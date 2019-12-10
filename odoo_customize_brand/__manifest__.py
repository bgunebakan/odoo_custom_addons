# -*- coding: utf-8 -*-

# Created on 2018-11-26
# author: Bilal Tonga, Creworker
# email: help@creworker.com
# Creworker
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# description:

{
    'name': 'Odoo Customize',
    'version': '13.19.11.24',
    'author': 'Creworker',
    'category': 'Productivity',
    'website': 'https://www.creworker.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """    
    Quick customize, debranding, boost, reset data, debug. Language Switcher. 
    Easy Delete data.reset account chart.
    odoo debrand, odoo debranding, customize my odoo. 
    """,
    'description': """
    
    App Odoo Customize(Debranding Title,Language,Documentation,Quick Debug)
    ============
    White label odoo.
    Support Odoo 13, 12, 11, 10, 9.
    You can config odoo, make it look like your own platform.
    1. Deletes Odoo label in footer
    2. Replaces "Odoo" in Windows title
    3. Customize Documentation, Support, About links and title in usermenu
    4. Adds "Developer mode" link to the top right-hand User Menu.
    5. Adds Quick Language Switcher to the top right-hand User Menu.
    6. Adds Country flags  to the top right-hand User Menu.
    7. Adds English and Chinese user documentation access to the top right-hand User Menu.
    8. Adds developer documentation access to the top right-hand User Menu.
    9. Customize "My odoo.com account" button
    10. Standalone setting panel, easy to setup.
    11. Provide 236 country flags.
    12. Multi-language Support.
    13. Change Powered by Odoo in login screen.(Please change '../views/odoo_customize_brand_view.xml' #15)
    14. Quick delete test data in Apps: Sales/POS/Purchase/MRP/Inventory/Accounting/Project/Message/Workflow etc.
    15. Reset All the Sequence to beginning of 1: SO/PO/MO/Invoice...
    16. Fix odoo reload module translation bug while enable english language
    17. Stop Odoo Auto Subscribe(Moved to app_odoo_boost)
    18. Show/Hide Author and Website in Apps Dashboard
    19. One Click to clear all data (Sometime pls click twice)
    20. Show quick upgrade in app dashboard, click to show module info not go to odoo.com
    21. Can clear and reset account chart. Be cautious
    22. Update online manual and developer document to odoo12
    23. Add reset or clear website blog data
    24. Customize Odoo Native Module(eg. Enterprise) Url
    25. Add remove expense data
    26. Add multi uninstall modules
    27. Add odoo boost modules link.
    
    This module can help to white label the Odoo.
    Also helpful for training and support for your odoo end-user.
    The user can get the help document just by one click.
    """,
    'images': ['static/description/banner.gif'],
    'depends': [
        'base_setup',
        'web',
        'mail',
        'iap',
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    'data': [
        'views/odoo_customize_brand_views.xml',
        'views/app_theme_config_settings_views.xml',
        'views/res_config_settings_views.xml',
        'views/ir_model_views.xml',
        'views/ir_views.xml',
        # data
        'data/ir_config_parameter.xml',
        'data/ir_module_module.xml',
        # 'data/digest_template_data.xml',
        'data/res_company_data.xml',
        'data/res_groups.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
