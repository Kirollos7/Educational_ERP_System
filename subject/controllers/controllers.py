# -*- coding: utf-8 -*-
# from odoo import http


# class Subject(http.Controller):
#     @http.route('/subject/subject/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subject/subject/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('subject.listing', {
#             'root': '/subject/subject',
#             'objects': http.request.env['subject.subject'].search([]),
#         })

#     @http.route('/subject/subject/objects/<model("subject.subject"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subject.object', {
#             'object': obj
#         })
