# -*- coding: utf-8 -*-
{
    'name': "Gestion de horarios",

    'summary': "Generacion de horarios para SGU",

    'description': """
MVP de gestión de horarios universitarios usando OpenEduCat
    """,

    'author': "Arturo Yanez",
    'website': "https://arutoyanez.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'openeducat_core','openeducat_timetable'],

    'assets': {
        'web.assets_backend': [
            "schedule/static/src/js/session_calendar_custom.js",
        ],
    },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/schedule_kanban_views.xml',
        'views/schedule_session_views.xml',
        'menus/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo_timetable.xml',
    ],
}

