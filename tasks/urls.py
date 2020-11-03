from django.urls import path, include
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_list/', views.add_list_tasks, name='add_list_tasks'),
    path('counter_list/', views.counter_lists, name='counter_lists'),
    path('list_tasks/', views.list_tasks, name='list_tasks'),
    path('lists/<int:id>/add_task', views.add_task, name='add_task'),
]