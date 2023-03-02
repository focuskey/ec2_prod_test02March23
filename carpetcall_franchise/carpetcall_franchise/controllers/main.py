from odoo import http
from odoo.http import request


class Books(http.Controller):
    @http.route("/books", auth='public', type='http')
    def list(self, **kwargs):
        Book = http.request.env['carpetcall.book']
        books = Book.search([])
        return http.request.render(
            "carpetcall_franchise.book_list_template",
            {"books": books}
        )
