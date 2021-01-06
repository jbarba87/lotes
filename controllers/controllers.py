# -*- coding: utf-8 -*-
from odoo import http

# class Lote(http.Controller):
#     @http.route('/lote/lote/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lote/lote/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lote.listing', {
#             'root': '/lote/lote',
#             'objects': http.request.env['lote.lote'].search([]),
#         })

#     @http.route('/lote/lote/objects/<model("lote.lote"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lote.object', {
#             'object': obj
#         })