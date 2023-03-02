from odoo import fields, models, api
from odoo.exceptions import ValidationError


# class Record(models.Model):
#     # _name = 'record.public'
#     _name = 'record.shareable'
#     _check_company_auto = True
#     _description = "mutil_company"
#
#     company_id = fields.Many2one('res.company')
#     other_record_id = fields.Many2one('other.record', check_company=True)
#
#     info = fields.Text()
#     company_info = fields.Text(company_dependent=True)
#     display_info = fields.Text(string='Infos', compute='_compute_display_info')
#
#     @api.depends_context('company')
#     def _compute_display_info(self):
#         for record in self:
#             record.display_info = record.info + record.company_info


# class Record(models.Model):
#     _name = 'record.restricted'
#     _check_company_auto = True
#
#     company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
#
#     other_record_id = fields.Many2one('other.record', check_company=True)


# class Record(models.Model):
#     _name = 'record.shareable'
#     _check_company_auto = True
#
#     company_id = fields.Many2one('res.company')
#     other_record_id = fields.Many2one('other.record', check_company=True)


# class Record(models.Model):
#     _name = 'record.restricted'
#     _check_company_auto = True
#
#     company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
#     other_record_id = fields.Many2one('other.record', check_company=True)
#


# class CompanyDetail(models.Model):
#     _name = 'company.detail'
#     _check_company_auto = True
#     _description = "Company_details"
#


class SecondModel(models.Model):
    _name = "carpetcall.book.lines"
    _description = "Lines"

    foreign_key = fields.Many2one(comodel_name="carpetcall.book", string="the new info")
    # foreign_key = fields.Many2one(comodel_name="product.image", string="the new info")
    # foreign_key = fields.Many2one(comodel_name="carpetcall.builder", string="Foreign_key")
    product_id = fields.Many2one('res.company', string="Name")
    product_qty = fields.Integer(string="Qty")


class Book(models.Model):
    """
    Describes a Book catalogue.
    """
    _name = "carpetcall.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book"
    _check_company_auto = True  # Maybe this is the key of the Mutil-company check
    # _check_company_auto = False
    _order = "name"
    # _table="carpetcall_book"


    name = fields.Char("Title", required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company,
                                 readonly=True)
    user_id = fields.Many2one('res.users', string='Technician', check_company=True)
    company_details = fields.Text(string="Company Details", company_dependent=True)

    product_lines = fields.One2many(comodel_name="carpetcall.book.lines",
                                    inverse_name="foreign_key")  # why the invers_name use "foreign_key" is ok, But I use product_id is wrong

    @api.onchange('company_details')
    def _onchange_company_details(self):
        self = self.with_company(self.company_id)

    @api.onchange('company_id')
    def _onchange_company_id(self):
        for rec in self:
            rec.company_details = 'self.env.user.company_id'
            # rec.company_details = 'testest'
            # rec.comment = "DDDD Changeer the company_id informatiofdfn!!!"

    # context['allowed_company_ids'][1])
    # company_id_s = fields.Char("Company_id_now")
    # company_id_s = lambda self: self.env.user
    # get_companyid = lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('carpetcall_franchise'))

    # lambda self: self.env.user.company_id )

    # default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('carpetcall_franchise')))

    # domain=['&&', ('company_id', 'in', 'company_ids'), ('company_id', '=', True)] )

    # domain=[('company_id', 'in', 'company_ids')])

    # default=lambda self: self.env.user.company_id)

    #### default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('your.module')))  #default=lambda self: self.env.user.company_id)#

    range = fields.Char("Range")
    sku = fields.Char("Sku", readonly=False)
    fibre = fields.Char("Fibre")  # , states={'readonly': True, 'invisible': False})
    colour = fields.Char("Colour")
    color = fields.Integer("Custom Widget Color")
    stock = fields.Char("Stock_code", readonly=False)  # , domain="[('stock', '=', 'self.env.user.company_id')]")
    # lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('carpetcall_franchise'))')]" )
    roll_type = fields.Char("Roll Type", readonly=False)
    retail_price = fields.Float('Retail Price', digits=(12, 2), readonly=False)
    roll_price = fields.Float('Roll Price', digits=(12, 2), readonly=False, compute="_compute_roll")
    floor_cost = fields.Float('Floor Cost', digits=(12, 2), groups="carpetcall_franchise.carpetcall_group_manager")
    roll_qty = fields.Float('Roll Quantity', digits=(12, 2))  # ,groups="carpetcall_franchise.carpetcall_group_usernor, carpetcall_franchise.carpetcall_group_manager")
    order_qty = fields.Float('Order Quantity', digits=(12, 2), default=0)  # groups="carpetcall_franchise.carpetcall_group_manager,carpetcall_franchise.carpetcall_group_user")
    free_qty = fields.Float('Free qty', digits=(12, 2), compute='_compute_free')  # , groups="carpetcall_franchise.carpetcall_group_manager, carpetcall_franchise.carpetcall_group_user")
    progress_qty = fields.Float(string='Progress Percent', compute="_compute_progress", recompute=True)
    discount = fields.Float('Discount_Franchise', tracking=True)
    total = fields.Float(compute='_compute_total')

    order_userno = fields.Float(string='Order', digits=(12, 2), tracking=True)
    left_userno = fields.Float(string='Remain', digits=(12, 2), readonly=True, compute="_compute_remail")



    def _compute_total(self):
        for record in self:
            record.total = record.retail_price * record.free_qty


    @api.model
    def _default_stage_id(self):
        Stage = self.env["carpetcall.book.stage"]
        # print(Stage)
        return Stage.search([("state", "=", "new")], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    stage_id = fields.Many2one(
        "carpetcall.book.stage",
        default=_default_stage_id,
        copy=False,
        group_expand="_group_expand_stage_id")

    state = fields.Selection(related="stage_id.state")

    def button_done0(self):
        Stage = self.env["carpetcall.book.stage"]
        done_stage = Stage.search([("state", "=", "open")], limit=1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True

    def button_done1(self):
        Stage = self.env["carpetcall.book.stage"]
        done_stage = Stage.search([("state", "=", "done")], limit=1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True

    def read_price(self):
        result = self.env['carpetcall.book'].read_group(
            domain=[],
            fields=['company_id', 'retail_price'],
            groupby=['company_id'],
            # aggregated={'retail_price': 'sum'}
            # lazy=False,
        )
        total = 0
        for group in result:
            total += group['retail_price']

        return total


        return result


    def read_price3(self):
        grouped_data = self.env['carpetcall.book'].read_group(
            domain=[],
            fields=['company_id', 'retail_price'],
            groupby=['company_id'],
           )
        return grouped_data


    def read_price4(self):
        grouped_data = self.env['carpetcall.book'].search(
            args=[],
            offset=0,
            limit=23,
            order=id,
            count=True
           )
        return grouped_data

    def read_price5(self):
        grouped_data = self.env['carpetcall.book'].read_group(
            [],
            fields=['company_id', 'retail_price'],
            groupby=['company_id'],
            lazy=False
        )

        for group in grouped_data:
            company_id = group['company_id'][0]
            sum_retail_price = group['retail_price']
            count = group['company_id']
            print("Company ID:", company_id, "Sum of Retail Price:", sum_retail_price, "Count:", count)


    def read_price2(self):
        results = self.env['carpetcall.book'].read_group(
            domain=[],
            fields=['company_id', 'retail_price'],
            groupby=['company_id'],
        )

        # for item in results:
        #     if item['company_id'][0] == 1:
        #         retail_price = results['retail_price']
        #         break
        # # print(retail_price)

        for item in results:
            if item['company_id'][0] == 1:
                print("Company ID: 1, Retail Price:", item['retail_price'])
            elif item['company_id'][0] == 2:
                print("Company ID: 2, Retail Price:", item['retail_price'])
            elif item['company_id'][0] == 3:
                print("Company ID: 3, Retail Price:", item['retail_price'])
            elif item['company_id'][0] == 4:
                print("Company ID: 4, Retail Price:", item['retail_price'])

        return True


    def max_value(self):
        record = self.search(
            [],
            order="retail_price desc",
            limit=1
        )
        return record.retail_price


    def dosql(self):
        query = """
        select company_id, sum(retail_price), count(*)
        from carpetcall_book
        group by company_id
        """
        self.env.cr.execute(query)
        self.env.cr.fetchall()


    def dosql2(self):
        query = """select id, name, retail_price from carpetcall_book"""
        self.env.cr.execute(query)
        # results = self.env.cr.dictfetchall()
        results = self.env.cr.dictfetchone()
        # print(results)
        return results

    def dosql3(self):
        query = """select id, name, stage_id, retail_price from carpetcall_book where stage_id = %s""" % self.env.uid
        self.env.cr.execute(query)
        # results = self.env.cr.dictfetchall()
        results = self.env.cr.dictfetchone()
        # print(results)
        return results



    def button_done2(self):
        Stage = self.env["carpetcall.book.stage"]
        print(Stage)
        done_stage = Stage.search([("state", "=", "cancel")], limit=1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True


    def button_done3(self):
        Stage = self.env["carpetcall.book.stage"]
        done_stage = Stage.search([("state", "=", "new")], limit=1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True

    @api.depends('roll_qty', 'order_qty', 'order_userno')
    def _compute_remail(self):
        for record in self:
            record.left_userno = record.roll_qty - record.order_qty - record.order_userno
            # if record.left_userno < 0:
            #     raise ValidationError("The Inventory Quantity is less then O!!! after count is: %s" % record.left_userno)
            #     # record.order_qty = 0;
            #     # record.order_userno=0;

    @api.constrains('order_userno')
    def _check_left_userno(self):
        if self.left_userno < 0:
            raise ValidationError(
                "The Inventory Quantity has not enought, %s will transfer this required to Sales persons to contact with you!" % self.left_userno)

    @api.depends("discount")
    def _compute_roll(self):
        for record in self:
            record.roll_price = record.retail_price * record.discount

    @api.depends('roll_qty', 'order_qty')
    def _compute_free(self):
        for record in self:
            if (record.order_qty > record.roll_qty):
                record.order_qty = record.roll_qty
            record.free_qty = record.roll_qty - record.order_qty


    @api.depends('roll_qty', 'free_qty', 'order_userno', 'left_userno')
    def _compute_progress(self):
        for record in self:
            if (record.roll_qty == 0):
                record.progress_qty = 0
                # record.free_qty = 0
            else:
                record.progress_qty = record.left_userno / record.roll_qty * 100

    @api.constrains('order_qty', 'roll_qty')
    def _check_freeqty(self):
        for record in self:
            if record.free_qty < 0:
                raise ValidationError("The Inventory Quantity is less then O!!! after count is: %s" % record.free_qty)

    # @api.depends("floor_cost")
    # def _compute_roll(self):
    #     for rec in self:
    #         rec.roll_price = rec.retail_price * rec.floor_cost

    parking_zone = fields.Selection([('a', 'AB'), ('b', 'BC'), ('c', 'CD')], string="Test_selection", copy='False',
                                    default='a')
    two_wheels = fields.Integer(string='Motor')
    four_wheels = fields.Integer(string='Mobile Umum')

    @api.onchange('parking_zone')
    def harge(self):
        for rec in self:
            if rec.parking_zone == 'a':
                rec.two_wheels = 2000
                rec.four_wheels = False
                rec.comment = "AAAA information!"
            elif rec.parking_zone == 'b':
                rec.two_wheels = False
                rec.four_wheels = 3000
                rec.comment = "BBBBB infomation!!!"
            elif rec.parking_zone == 'c':
                rec.two_wheels = 1000
                rec.four_wheels = 2600
                rec.comment = "CCCCC information!!!"
                rec.roll_qty = 0
                rec.floor_cost = 0
                rec.order_qty = 0
                rec.free_qty = 0
                rec.isbn = 0

    comment = fields.Text("Comment", tracking=True, default="This is the commment to edit fields.")

    # comment = fields.Text("Comment", read=['carpetcall_franchise.carpetcall_group_user'], write=['carpetcall_franchise.carpetcall_group_manager'], default="This is the commment to edit fields.")

    # parterid = fields.many2one('res.partner', 'Customer', readonly=True,
    #                 states={'draft': [('readonly', False)], 'sent': [('readonly', False)],
    #                         'test': [('readonly', False)]}, required=True, change_default=True, select=True,
    #                 track_visibility='always')

    isbn = fields.Char(string="Status_Code")

    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date(string="Date Provided")
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Supplier")
    # build_id = fields.Many2one("public.builder", string="Builder")
    build_id = fields.Many2one("carpetcall.builder", string="Builder")
    # product_lines = fields.One2many('carpetcall.book.lines', 'foreign_key')

    discount2 = fields.Float(string="Discount", tracking=True, default=1, groups="carpetcall_franchise.carpetcall_group_manager, carpetcall_franchise.carpetcall_group_user, carpetcall_franchise.carpetcall_group_usernor" )  # related="build_id.discount",

    # discount3 = fields.Float(string="DISCOUNT", tracking=True)
    # serial_no2 = fields.Char(string="Serial_no_build", related="build.id.serial_no")

    @api.constrains('discount2')
    def _check_discout2(self):
        if self.discount2 < 0.3:
            raise ValidationError("You sell it at a very very low discount : %s less then 0.3, No!!!" % self.discount2)

    @api.depends("discount2")
    def _compute_roll(self):
        for record in self:
            record.roll_price = record.retail_price * record.discount2

    builder_name = fields.Char(string="Build_Name", related="build_id.name")
    builder_phone = fields.Char(string="Build_Phone", related="build_id.mobie")
    builder_address = fields.Char(string="Build_address", related="build_id.address")
    # function_info = fields.Many2one("res.partner", string="NameFunction", domain=[('id', '=', 'publisher_id')])
    # function_info = fields.Many2one("res.partner.function", string="NameFun")
    function_info = fields.Char(string='Supplier_Info',
                                related="publisher_id.function")  # , domain=[('id', '=', 'publisher_id')])
    address_info = fields.Char(string="The Supplier Address", related="publisher_id.street")
    tel_info = fields.Char(string="The Supplier phone", related="publisher_id.phone")
    author_ids = fields.Many2many(comodel_name="res.partner", string="Contact")

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        # print(self.env)
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
        return True

    _sql_constraints = [
        ("name",
         # "UNIQUE (name, date_published)", # the name and the date_published together both  same , arise error
         "UNIQUE(name)",  # Only check the name, if the name is same, there will be an  error arise
         "Title (name) must be unique."),
        # ("carpetcall_book_check_date",
        #  "CHECK (date_published >= current_date)",
        #  "Publication date must not be in the future."),
    ]
