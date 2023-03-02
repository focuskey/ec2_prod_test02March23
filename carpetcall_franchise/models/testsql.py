from odoo import models, fields, api


class TestSql(models.Model):
    _name = "carpetcall_franchise.testsql"
    _description = "carpetcall_franchise.TestSql"
    _auto = True

    sale_number = fields.Char('Sales Number')
    customer_name = fields.Char('Customer')
    order_date = fields.Datetime('Order Date')
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company, readonly=True)
    company_details = fields.Text(string="Company Details", company_dependent=True)
    # amount = fields.Monetary('Amount')
    # currency_id = fields.Many2one('res.currency', string='Currency')

    def init_change(self):
        self.env.cr.execute("""select name as sale_number from res_partner""")
        self.env.cr.fetchall()

    def init(self):
        self.env.cr.execute("""
        select rs.display_name as sale_number, rs.email as customer_name
        from res_partner rs
        """)
        self.env.cr.fetchall()

        # select name as sale_number, sku as customer_name, date_published as order_date
        # from carpetcall_book


    @api.onchange('company_id')
    def _onchange_company_id(self):
        for rec in self:
            rec.company_details = 'self.env.user.company_id'

    @api.onchange('company_details')
    def _onchange_company_details(self):
        self = self.with_company(self.company_id)


    def init_old(self):
        self._cr.execute("""
        CREATE OR REPLACE VIEW sale_sql_view AS (
        SELECT row_number() OVER() as id,
        so.name as sale_number,
        rp.name as customer_name,
        so.date_order as oder_date,
        so.amount_total as amount,
        rc.id as currency_id
        FROM sale_order so
        JOIN res_partner rp ON so.partner_id = rp.id
        JOIN res_currency rc ON so.currency_id = rc.id        
        )        
        """)

