from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from tasks.models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')

    paginador = Paginator(tasks, 10)
    page_number = request.GET.get('page')
    page_object = paginador.get_page(page_number)

    if request.headers.get('HX-Request'):
        return render(request, 'partials/task_list.html', {'page_object': page_object})

    return render(request, 'index.html', {'page_object': page_object})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            response = render(request, 'partials/task_item.html', {'task' : task})
            response['HX-Trigger'] = 'close-modal'
            response['HX-Refresh'] = 'true'
            return response

        return render(request, 'partials/task_modal_content.html', {
            'form': form,
            'modal_title': 'Nova Tarefa'
        })

    # GET: Formulário limpo
    form = TaskForm()
    return render(request, 'partials/task_modal_content.html', {
        'form': form,
        'modal_title': 'Nova Tarefa'
    })

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return render(request, 'partials/task_item.html', {'task' : task})
        return HttpResponse("Erro ao atualizar", status=400)

    return render(request, 'partials/task_modal_content.html', {'task' : task, 'modal_title': 'Editar Tarefa'})

'''
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponse("")
'''

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse("")

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()

    return render(request, 'partials/task_item.html', {'task' : task})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk,  user=request.user)
    return render(request, 'partials/task_detail.html', {'task' : task})