# -*- coding: utf-8 -*-
{
    'name':"To Do Managemant",
    'summary': " To Do management list by day  ",

    'description': """
     Long description of module's purpose
      To Do management list by day 
      and have view tree , form and
       have search view .
    """,

    'author': "Mohamed Abdalla Ashmawi ",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '17.0.0.0.1',
    # any module necessary for this one to work correctly
    'depends': ['base' ,'mail'],

    # always loaded
    'data': [
        'security /ir.model.access.csv',
        'views/todo_view.xml',
        # 'views/templates.xml',
    ],

}