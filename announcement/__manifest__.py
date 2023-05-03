{
    'name': 'Announcement',

    'summary': """""",
    'description': """""",

    'category': '',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base'],
    'data': [

             ],
    'assets': {
       'web.assets_backend': [
           # 'announcement/static/src/js/announcement_systray.js',
           'announcement/static/src/js/systray.js',
           'announcement/static/src/xml/accouncement_template.xml',
       ],
   },

    # 'images': ['static/description/banner.png'],
    # 'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
