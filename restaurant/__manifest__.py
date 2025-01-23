# -*- coding: utf-8 -*-
{
    'name': "Restaurant Ext",

    'summary': "this module is all about Restaurant",

    'description': """
this module is all about Restaurant
    """,

    'author': "Murtaza Alam",

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/restaurant_ext.xml',

    ],
    'images': ['static/description/icon.png']

}
