{
    'name': 'Product Variant Comparison',
    'version': '16.0.1.0.0',
    'summary': """
    valuation""",
    'category': '',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'website', 'website_sale','product','web'],
    'website': 'https://www.cybrosys.com',
    'data': ['security/ir.model.access.csv', 'views/product_product_views.xml',
             'views/product_specs_templates.xml', 'views/variant_compare_views.xml',
             'views/product_compare_button_template.xml'
             ],
    'assets': {'web.assets_frontend': ['product_variant_comparison/static/src/css/specs.css',
        'product_variant_comparison/static/src/js/variant_compare.js']},
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
