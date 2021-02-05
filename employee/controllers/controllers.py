# -*- coding: utf-8 -*-
# from odoo import http


# class Employee(http.Controller):
#     @http.route('/employee/employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee/employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee.listing', {
#             'root': '/employee/employee',
#             'objects': http.request.env['employee.employee'].search([]),
#         })

#     @http.route('/employee/employee/objects/<model("employee.employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee.object', {
#             'object': obj
#         })
