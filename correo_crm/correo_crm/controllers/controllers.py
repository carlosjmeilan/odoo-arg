# -*- coding: utf-8 -*-
from odoo import http
from odoo import models

# class CorreoCrm(http.Controller):
#     @http.route('/correo_crm/correo_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/correo_crm/correo_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('correo_crm.listing', {
#             'root': '/correo_crm/correo_crm',
#             'objects': http.request.env['correo_crm.correo_crm'].search([]),
#         })

#     @http.route('/correo_crm/correo_crm/objects/<model("correo_crm.correo_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('correo_crm.object', {
#             'object': obj
#         })
