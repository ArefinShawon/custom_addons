{
    'name': 'Dynamic Purchase Order Approval/Purchase Approval',
    'version': 'v16',
    'description': """
    Purchase order approval system. 
    Any authorized designated user who is a member of PO approval team can approve the purchase. Without every members approval a purchase cannot be confirmed.
    However the team lead of that team can directly confirm the purchase order even if any member's approval state is pending. 
    """,
    'category': 'Purchase',
    'summary': 'Dynamic, Customizable and Flexible Approval Process for Purchase Orders',
    'author': 'Shawon',
    'license': 'LGPL-3',
    'depends': ['base', 'purchase'],
    'data': [
        'views/purchase_order_teams_views.xml',
        'views/purchase_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
