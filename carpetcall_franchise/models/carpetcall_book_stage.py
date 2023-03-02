from odoo import fields, models


class CarpetCallStage(models.Model):
    _name = "carpetcall.book.stage"
    _description = "Carpetcall stage"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("new", "Requested"),
            ("open", "Operating"),
            ("done", "Finished"),
            ("cancel", "Canceled")],
        default="new",)
