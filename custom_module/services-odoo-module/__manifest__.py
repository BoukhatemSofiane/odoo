# -*- coding: utf-8 -*-
{
    'name': 'Services Management',
    'version': '1.0.0',
    'summary': 'Manage and deliver professional services',
    'sequence': 10,
    'description': """
Services Management Module
===========================
This module helps manage services such as consulting, maintenance, or support. It includes features to track service requests, allocate resources, and generate invoices.
    """,
    'category': 'Services',
    'author': 'Sofiane',
    'license': 'LGPL-3',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/service_views.xml',
        'data/services_data.xml',
    ],
    'images': [
    
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
