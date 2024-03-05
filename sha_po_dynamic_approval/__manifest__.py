{
    'name': 'Purchase Order Dynamic Approval',
    'version': 'v16',
    'category': 'Inventory/Purchase',
    'summary': 'Dynamic, Customizable and Flexible Approval Process for Purchase Orders',
    'author': 'shawon',
    'license': 'LGPL-3',
    'depends': ['base', 'purchase'],
    'data': [
        'views/purchase_order_teams_views.xml',
        'views/purchase_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
