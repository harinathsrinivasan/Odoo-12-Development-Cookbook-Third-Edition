# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """Long description""",  # You can also rst format
    'author': "Your name",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base', 'decimal_precision'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'data/data.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    'demo': [
        'data/demo.xml'
    ],
}
