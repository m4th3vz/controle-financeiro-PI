# shopping_list/urls.py
from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView

urlpatterns = [
    path('task_list', TaskListView.as_view(), name='task_list'),
    path('task_add/', TaskCreateView.as_view(), name='task_add'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
