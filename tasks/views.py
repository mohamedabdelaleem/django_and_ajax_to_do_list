from django.shortcuts import render
from .models import ListTask, Task
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

def home(request):
    """ return home bag """
    lists = ListTask.objects.all()
    return render(request, 'to_do.html', {'lists':lists})


def counter_lists(request):
    """ return number of lists task 'to make Some additions in template' """
    lists = ListTask.objects.all()
    data = {'list_num':len(lists)}
    return JsonResponse(data)

def add_list_tasks(request):
    """ add a new list tasks"""
    list_name = request.GET['name']
    new_list = ListTask.objects.create(name=list_name)
    data = {'new_list':new_list.name,'id':new_list.id}
    return JsonResponse(data)


def return_list_tasks(request):
    """ return a list_tasks detail"""
    print(request.GET['id'])
    list_tasks = ListTask.objects.get(id=request.GET['id'])
    tasks = list_tasks.task_set.all()
    tasks_info = []
    for task in tasks:
        tasks_info.append({'name':task.name,'id':task.id})

    data = {
            'list_name':list_tasks.name,
            'id':list_tasks.id,
            'tasks_num':len(tasks),
            'tasks':tasks_info,
        }
    return JsonResponse(data)


