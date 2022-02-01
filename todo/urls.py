from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_content, name='list'),
    path('update/<str:pk>/', views.update_tasks, name='update'),
    path('delete/<str:pk>/', views.delete_tasks, name='delete'),
]
