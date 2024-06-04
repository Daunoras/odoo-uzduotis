# -*- coding: utf-8 -*-
# from odoo import http


# class Uzduotis(http.Controller):
#     @http.route('/uzduotis/uzduotis', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uzduotis/uzduotis/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uzduotis.listing', {
#             'root': '/uzduotis/uzduotis',
#             'objects': http.request.env['uzduotis.uzduotis'].search([]),
#         })

#     @http.route('/uzduotis/uzduotis/objects/<model("uzduotis.uzduotis"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uzduotis.object', {
#             'object': obj
#         })

