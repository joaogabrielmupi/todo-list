from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.TaskCreateView.as_view(), name='create-task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete-task'),
    path('update/<int:pk>/', views.update_task_status, name='update-task'),
    path('edit/<int:pk>/', views.TaskUpdateView.as_view(), name='edit-task'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),

]