# -*- coding: utf-8 -*-
# from odoo import http


# class Management(http.Controller):
#     @http.route('/management/management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/management/management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('management.listing', {
#             'root': '/management/management',
#             'objects': http.request.env['management.management'].search([]),
#         })

#     @http.route('/management/management/objects/<model("management.management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('management.object', {
#             'object': obj
#         })
