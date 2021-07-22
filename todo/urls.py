from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('list/', allContent, name='list'),
    path('update/<str:pk>/', updateTasks, name='update'),
    path('delete/<str:pk>/', deleteTasks, name='delete'),

]