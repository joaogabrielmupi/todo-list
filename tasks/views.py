from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from tasks.models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()

            return  render(request, 'partials/task_item.html', {'task' : task})

        return HttpResponse('Dados inválidos', status=400)


    return render(request, 'partials/task_modal_content.html', {'modal_title' : 'Nova Tarefa'})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return render(request, 'partials/task_item.html', {'task' : task})
        return HttpResponse("Erro ao atualizar", status=400)

    return render(request, 'partials/task_modal_content.html', {'task' : task, 'modal_title': 'Editar Tarefa'})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponse("")

def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()

    return render(request, 'partials/task_item.html', {'task' : task})