from odoo import fields, models, tools
from odoo.exceptions import ValidationError


class builder(models.Model):
    """
    Describes a Book catalogue.
    """
    _name = "carpetcall.builder"
    _description = "Builder"

    name = fields.Char("Name", required=True, readonly=False)
    mobie = fields.Char("Mobie")
    address = fields.Char("Address")
    builder_name = fields.Char("Builder_Name")
    serial_no = fields.Char("Serial_no", index=True)

    discount = fields.Float('Discount_b', readonly=False, default=1, groups="carpetcall_franchise.carpetcall_group_user")

    # fibre = fields.Char("Fibre")
    # colour = fields.Char("Colour")
    # stock = fields.Char("Stock_code", readonly=False)
    # # roll_type = fields.Char("Roll Type")
    # retail_price = fields.Float('Retail Price', digits=(12, 2))
    # roll_price = fields.Float('Roll Price', digits=(12, 2))
    # floor_cost = fields.Float('Floor Cost', digits=(12, 2))
    # roll_qty = fields.Float('Roll Quantity', digits=(12, 2))
    # order_qty = fields.Float('Order Quantity', digits=(12, 2), groups="carpetcall_franchise.carpetcall_group_manager")
    # free_qty = fields.Float('Free qty', digits=(12, 2))
    #
    # isbn = fields.Char(string="Status_Code")
    # active = fields.Boolean("Active?", default=True)
    # date_published = fields.Date(string="Date Provided")
    # image = fields.Binary("Cover")
    # publisher_id = fields.Many2one("res.partner", string="Supplier")
    # build_id = fields.Many2one("public.builder", string="Builder")
    # # function_info = fields.Many2one("res.partner", string="NameFunction", domain=[('id', '=', 'publisher_id')])
    # # function_info = fields.Many2one("res.partner.function", string="NameFun")
    # function_info = fields.Char(string='Funcs', related="publisher_id.function") #, domain=[('id', '=', 'publisher_id')])
    # address_info = fields.Char(string="The Address", related="publisher_id.street")
    # tel_info = fields.Char(string="The Telephone", related="publisher_id.phone")
    #
    # # builder_name = fields.Char(string="Build_Name", related="build_id.builder_name")
    #
    # author_ids = fields.Many2many("res.partner", string="Contact")
