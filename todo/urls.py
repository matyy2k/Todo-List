from django.urls import path
from . import views

urlpatterns = [
    path('', views.allContent, name='list'),
    path('update/<str:pk>/', views.updateTasks, name='update'),
    path('delete/<str:pk>/', views.deleteTasks, name='delete'),

]