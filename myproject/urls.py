from django.contrib import admin
from django.urls import path, include
from todo.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'todo', TodoView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('api', include(router.urls)),
]