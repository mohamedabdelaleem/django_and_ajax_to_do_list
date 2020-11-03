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
    data = {'lists_num':len(lists)}
    return JsonResponse(data)

def add_list_tasks(request):
    """ add a new list tasks"""
    list_name = request.GET['name']
    new_list = ListTask.objects.create(name=list_name)
    data = {'new_list':new_list.name,'id':new_list.id}
    return JsonResponse(data)


def list_tasks(request):
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


def add_task(request, id):
    """ add task to list """
    task_name = request.GET['task_name']
    list_tasks = ListTask.objects.get(id=id)
    new_task = Task.objects.create(list_tasks=list_tasks, name=task_name)
    tasks_counter = Task.objects.filter(list_tasks=list_tasks)
    data = {'task_name':task_name, 'task_id':new_task.id, 'tasks_num':len(tasks_counter)}
    return JsonResponse(data)


