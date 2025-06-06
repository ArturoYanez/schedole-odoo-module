# -*- coding: utf-8 -*-
# from odoo import http
#
#
# class Schedule(http.Controller):
#     @http.route('/schedule/schedule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"
#
#     @http.route('/schedule/schedule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('schedule.listing', {
#             'root': '/schedule/schedule',
#             'objects': http.request.env['schedule.schedule'].search([]),
#         })
#
#     @http.route('/schedule/schedule/objects/<model("schedule.schedule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('schedule.object', {
#             'object': obj
#         })
#
