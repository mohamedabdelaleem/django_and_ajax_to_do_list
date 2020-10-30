from django.urls import path, include
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/add_list/', views.add_list_tasks, name='add_list_tasks'),
    path('counter_list/', views.counter_lists, name='counter_lists'),
    path('list_tasks/', views.return_list_tasks, name='return_list_tasks'),
]