{
    'name': 'My Contact Module',
    'category': 'Sales/CRM',
    'summary': 'Contact management module for Thu Cuc tesing',
    'version': '1.0',
    'category': 'Customer Relationship Management',
    'author': 'Khang Khang',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/contact_views.xml',
    ],
    'installable': True,
    'application': True,
}
