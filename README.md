# Todo-List 
## Table of Contents

* General info
* Technologies
* How to run


## General info
My first self-written app. This is a simple todo list. 
Includes CRUD - allows you to create, modify and delete tasks.  
A login and registration system has been introduced, and each user has an individual list of tasks.  
CSS is based on the Bootstrap toolkit.


## Technologies
- Python 3.9.5
- Django 3.2.5


## How to run
Change your settings.py  
1) 
```
INSTALLED_APPS = [
    ...
    'todo',
]
```
2)
```
TEMPLATES = [
    {
        ...
        'DIRS': ['templates'],
        'APP_DIRS': True,
        ...
```
3)
```
STATIC_URL = '/static/'
STATICFILES_DIRS = ['my_static']
```

4)

```
pip install -r requirements.txt
```

5) U can create new user or login to admin
```
Login: admin
Password: admin
```



