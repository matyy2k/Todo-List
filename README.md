# Todo-List
My first self-written app. This is a simple todo list. 
Includes CRUD - allows you to create, modify and delete tasks.
CSS is based on the Bootstrap toolkit


How to run app:
1) Add 'todo' in settings.py
INSTALLED_APPS = [
    ...
    'todo',
]

2) Add in settings.py
TEMPLATES = [
    {
        ...
        'DIRS': ['templates'],
        'APP_DIRS': True,
        ...


3) Add in settings:
STATIC_URL = '/static/'
STATICFILES_DIRS = ['myStatic']



