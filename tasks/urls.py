from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('update/<int:pk>/', views.update_task_status, name='update-task'),
    path('edit/<int:pk>/', views.edit_task, name='edit-task'),
]