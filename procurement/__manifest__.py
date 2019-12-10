# -*- coding: utf-8 -*-

{
    'name': 'Procurement',
    'version': '13.0.1.0.1',
    'category': 'Accounting',
    'summary': 'Procurement for Odoo13 Community Edition',
    'live_test_url': 'https://creworker.com',
    'sequence': '8',
    'author': 'Creworker',
    'maintainer': 'Creworker',
    'license': 'LGPL-3',
    'support': 'help@creworker.com',
    'website': '',
    'depends': ['mail','hr'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/tender.xml',
        'reports/report.xml',
        'reports/tender_overview.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'images': ['static/description/banner.gif'],
    'qweb': [],
}
