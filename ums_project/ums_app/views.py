from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from django.core.paginator import Paginator


def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('create_task')  # Redirect to the home page
    else:
        serializer = TaskSerializer()

    tasks = Task.objects.all()
    search_query = request.GET.get('search')

    if search_query:
        tasks = tasks.filter(id=search_query)

    paginator = Paginator(tasks, 5)  # Set the number of tasks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'create_task.html', {'serializer': serializer, 'tasks': tasks, 'page_obj': page_obj, 'search_results': tasks})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        serializer = TaskSerializer(instance=task, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('create_task')  # Redirect to the task list page
    else:
        serializer = TaskSerializer(instance=task)
    return render(request, 'update_task.html', {'serializer': serializer, 'task_id': task_id, 'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('create_task')  # Redirect to the home page
    return render(request, 'delete_task.html', {'task_id': task_id})
