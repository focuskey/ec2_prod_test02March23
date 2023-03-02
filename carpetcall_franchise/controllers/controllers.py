from odoo import http
from odoo.http import request


class WebsiteSale(http.Controller):

    @http.route('/shop/cart', type='http', auth="public", website=True)
    def shop_cart(self, **post):
        return request.redirect('/shop/checkout')




# -*- coding: utf-8 -*-
# from odoo import http


# class CarpetcallFranchise(http.Controller):
#     @http.route('/carpetcall_franchise/carpetcall_franchise', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carpetcall_franchise/carpetcall_franchise/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carpetcall_franchise.listing', {
#             'root': '/carpetcall_franchise/carpetcall_franchise',
#             'objects': http.request.env['carpetcall_franchise.carpetcall_franchise'].search([]),
#         })

#     @http.route('/carpetcall_franchise/carpetcall_franchise/objects/<model("carpetcall_franchise.carpetcall_franchise"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carpetcall_franchise.object', {
#             'object': obj
#         })
