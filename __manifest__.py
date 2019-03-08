# -*- coding: utf-8 -*-
{
    'name': "Modulo Pruebas - Anthony",

    'summary': """
        Un modulo de pruebas""",

    'description': """
        Modulo que funcionara para pruebas
    """,

    'author': "Anthony J.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Puebas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}