from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create-task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete-task'),
    path('update/<int:pk>/', views.update_task_status, name='update-task'),
    path('edit/<int:pk>/', views.edit_task, name='edit-task'),
    path('task/<int:pk>/', views.task_detail, name='task-detail'),

]