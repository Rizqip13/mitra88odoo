# -*- coding: utf-8 -*-
# from odoo import http


# class Sikilat(http.Controller):
#     @http.route('/sikilat/sikilat', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sikilat/sikilat/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sikilat.listing', {
#             'root': '/sikilat/sikilat',
#             'objects': http.request.env['sikilat.sikilat'].search([]),
#         })

#     @http.route('/sikilat/sikilat/objects/<model("sikilat.sikilat"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sikilat.object', {
#             'object': obj
#         })
