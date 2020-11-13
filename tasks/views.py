from django.shortcuts import render
from .models import ListTask, Task
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here..

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
    list_tasks = ListTask.objects.get(id=request.GET['id'])
    tasks = list_tasks.task_set.all()
    tasks_remaining = len(tasks.filter(is_done=False))
    tasks_info = []
    for task in tasks:
        if task.is_done:
            tasks_info.append({'name':task.name,'id':task.id, 'is_checked':'checked'})  # here i give the value 'checked' to التعويض عنها in the checkpox
        else:
            tasks_info.append({'name':task.name,'id':task.id, 'is_checked':''})

    data = {
            'list_name':list_tasks.name,
            'id':list_tasks.id,
            'tasks_remaining':tasks_remaining,
            'tasks':tasks_info,
        }
    return JsonResponse(data)


def add_task(request, id):
    """ add task to list """
    task_name = request.GET['task_name']
    list_tasks = ListTask.objects.get(id=id)
    new_task = Task.objects.create(list_tasks=list_tasks, name=task_name)
    tasks = Task.objects.filter(list_tasks=list_tasks)
    tasks_remaining = len(tasks.filter(is_done=False))
    data = {'task_name':task_name, 'task_id':new_task.id, 'tasks_remaining':tasks_remaining}
    return JsonResponse(data)


def task_status(request):
    """ Complete the task or cancel it if done """
    task_id = request.GET['id']
    task = Task.objects.get(id=task_id)
    if task.is_done:
        task.is_done = False
        task.save()
    else:
        task.is_done = True
        task.save()

    tasks = Task.objects.filter(list_tasks=task.list_tasks)
    tasks_remaining = len(tasks.filter(is_done=False))
    
    data = {'is_done':task.is_done, 'tasks_remaining':tasks_remaining}
    return JsonResponse(data)


def clear_tasks(request):
    """ delete completed tasks """
    list_id = request.GET['id']
    list_tasks = ListTask.objects.get(id=list_id)
    tasks = Task.objects.filter(list_tasks=list_tasks, is_done=True)
    if len(tasks) >= 1:
        tasks.delete()
        data = {'done':True}
    else:
        data = {'done':False}

    return JsonResponse(data)


def delete_list(request):
    
    list_id = request.GET['id']
    list_tasks = ListTask.objects.get(id=list_id)
    if list_tasks:
        list_tasks.delete()
        data = {'deleted':True}
    else:
        data = {'deleted':False}
    return JsonResponse(data)
