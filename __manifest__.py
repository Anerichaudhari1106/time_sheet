# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Time_sheet',
    'version': '1.4',
    'category': 'time_sheet/time_sheet',
    'summary': 'Time_sheet internal machinery',

    'depends': ['base'],

    'data': [
            'security/ir.model.access.csv',
             'views/project_views.xml',
             'views/task_views.xml'


             ],

    'demo': [],

    'installable': True,
    'assets': {

    },
    'license': 'LGPL-3',

}
