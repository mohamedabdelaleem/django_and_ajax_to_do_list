from django.urls import path, include
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_list/', views.add_list_tasks, name='add_list_tasks'),
    path('counter_list/', views.counter_lists, name='counter_lists'),
    path('list_tasks/', views.list_tasks, name='list_tasks'),
    path('task_status/', views.task_status, name='task_status'),
    path('delete_complete_tasks/', views.clear_tasks, name='clear_tasks'),
    path('delete_list_tasks/', views.delete_list, name='delete_list'),
    path('lists/<int:id>/add_task', views.add_task, name='add_task'),
]