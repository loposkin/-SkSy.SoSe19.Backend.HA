from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms.TodoForm import TodoForm
from .models import Task
from datetime import datetime


def index(request):
    task_list = Task.objects.order_by('-pub_date')
    context = {
        'task_list' : task_list,
    }
    return render(request, 'todo/index.html', context)


def about(request):
    return render(request, 'todo/impressum.html')


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            task = Task(deadline=form.cleaned_data['date'],
                        task_text=form.cleaned_data['text'],
                        progress=form.cleaned_data['percent'],
                        pub_date=datetime.now())
            task.save()
            return HttpResponseRedirect(reverse('todo:index'))
        else:
            # form = TodoForm()
            return render(request, 'todo/create-todo.html', {'form': form})
    else:

        return render(request, 'todo/create-todo.html')


def edit_todo(request, todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            task.deadline = form.cleaned_data['date']
            task.task_text = form.cleaned_data['text']
            task.progress = form.cleaned_data['percent']
            task.save()
            return HttpResponseRedirect(reverse('todo:index'))
        else:
            # form = TodoForm()
            return render(request, 'todo/edit-todo.html', {'form': form})
    form = TodoForm(initial={'text': task.task_text, 'percent': task.progress, 'date': task.deadline})
    return render(request, 'todo/edit-todo.html', {'form': form})


def delete_todo(request, todo_id):
    return render(request, 'todo/index.html', context)
