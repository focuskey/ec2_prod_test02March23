from odoo import fields, models, tools
from odoo.exceptions import ValidationError

class partner_product(models.Model):
    _name = 'carpetcall_franchise.partner_product'
    _auto = False
    _description = 'carpetcall_franchise.partner_product'

    name = fields.Char("Partner Name")
    product_name = fields.Char("Product Name")
    display_name = fields.Char("Display_name")
    total_quantity_sold = fields.Char("Total Quantity Sold")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))

    def _query(self, with_clause="", fields={}, groupby="", from_clause=""):
        return """
            SELECT

            T1.id,
            pr.name "name",
            pt.name "product_name",
            pr.display_name "display_name",
            T1."total_quantity_sold"


            FROM 

            (
            SELECT

            p.id,
            sum(sol.product_uom_qty) "total_quantity_sold"

            FROM

            product_product p
            inner join sale_order_line sol on sol.product_id = p.id
            inner join sale_order so on so.id=sol.order_id


            where so.state ='done'
            or so.state='sale'

            GROUP BY
            p.id

            )T1

            inner join product_product prod on prod.id=T1.id
            inner join sale_order_line sol on sol.product_id =prod.id
            inner join product_template pt on pt.id = prod.product_tmpl_id
            inner join sale_order so on so.id=sol.order_id
            inner join res_partner pr on so.partner_id=pr.id


            where so.state ='done'
            or so.state='sale'

            GROUP BY
            T1.id,
            pr.name,
            pr.display_name,
            pt.name,
            T1."total_quantity_sold"
            """


    def _query_test(self, with_clause="", fields={}, groupby="", from_clause=""):
        return """
            SELECT * FROM res_company
            """