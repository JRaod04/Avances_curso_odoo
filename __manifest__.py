{
	'name': 'grades_manager',
	'summary': 'Handles grades among students and curses',
	'description' : 'Handles grades among students and curses',
	'author' : 'JoseJ04',
	'category' : 'Base',
	'version' : '18.0.0.1',
	'depends' : ['base'],
	'data' : [
        'security/ir.model.access.csv',
        'views/grades_course_view.xml',
        'views/grades_teacher_views.xml',
        'views/grades_manager_menus.xml',
    ],
	'license' : 'AGPL-3',
    'application': True,
	'installable' : True,
	'auto_install' : False
}