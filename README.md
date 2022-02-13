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
Simple API is also available. There you can see a list of tasks for all users.  
The user list is only available to the administrator.


## Technologies
- Python 3.9.5
- Django 4.0


## How to run

* You can open the website online:
https://todo-list-djangoapp.herokuapp.com/

Log in to default user:

login: User  
password: Usertest1

or create new user...

* You can create applications locally on your computer:

1) git clone https://github.com/matyy2k/Todo-List.git
2) pip install -r requirements-dev.txt
3) python manage.py migrate
4) python manage.py runserver






