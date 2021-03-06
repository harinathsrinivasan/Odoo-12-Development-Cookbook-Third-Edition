# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """Long description""",  # You can also rst format
    'author': "Your name",
    'website': "http://www.example.com",
    'category': 'Library',
    'version': '12.0.1',
    'depends': ['base_setup'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/library_book.xml',
        'views/res_config_settings.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
