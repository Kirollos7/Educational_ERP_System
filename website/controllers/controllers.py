# -*- coding: utf-8 -*-
# from odoo import http


# class Website(http.Controller):
#     @http.route('/website/website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website/website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website.listing', {
#             'root': '/website/website',
#             'objects': http.request.env['website.website'].search([]),
#         })

#     @http.route('/website/website/objects/<model("website.website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website.object', {
#             'object': obj
#         })
