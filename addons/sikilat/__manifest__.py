# -*- coding: utf-8 -*-
{
    'name': "sikilat delivery",

    'summary': """
        An external Shipping Provider""",

    'description': """
        Add option to use Sikilay Delivery service
    """,

    'author': "Sikilat",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "delivery"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sikilat_delivery.xml',
        'views/sikilat_driver.xml',
        'views/sikilat_vehicle.xml',
        'views/sikilat_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
