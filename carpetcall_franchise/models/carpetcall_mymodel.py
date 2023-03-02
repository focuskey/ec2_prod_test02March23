from odoo import models, fields


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    website_published = fields.Boolean(string='Published on Website', default=True)


