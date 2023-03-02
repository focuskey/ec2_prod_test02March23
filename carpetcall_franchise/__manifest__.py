# -*- coding: utf-8 -*-
{
    'name': "carpetcall_franchise",
    'summary': "CarpetCall Franchise Business Type",
    'author': "William WEI",
    "license": "AGPL-3",
    'website': "https://www.carpetcall.com.au",
    "version": "15.0.1.0.0",
    "category": "Services/CarpetCall",
    "depends": ["base", "mail", "web", "product"],
    "data": [
        "security/carpetcall_security.xml",
        "security/ir.model.access.csv",
        "views/carpetcall_view.xml",
        "views/carpetcall_menu.xml",
        "views/carpetcall_product_view.xml",
        "views/book_list_template.xml",
        # "views/website_form.xml",
        # "views/templates.xml",
        # "static/src/descripe.css",
        # "views/carpet_list_template.xml",
        "reports/carpetcall_book_report.xml",
        "data/carpetcall_book_stage.xml",
        ],
    'assets': {
        'web.assets_backend': [
            'carpetcall_franchise/static/src/js/field_widget.js',
        ],
        'web.assets_common': [
            'carpetcall_franchise/static/src/scss/field_widget.scss',
        ],
    },
    "application": True,
}