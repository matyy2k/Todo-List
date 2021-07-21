from django.shortcuts import render, redirect
from .models import *
from .forms import *


def allContent(request):
    all = Content.objects.all()

    form = TasksForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'tasks': all, 'form': form}
    return render(request, 'todo.html', context)

def updateTasks(request, pk):
    task = Content.objects.get(id=pk)

    form = TasksForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('list')

    context = {'form': form}
    return render(request, 'update.html', context)

def deleteTasks(request, pk):
    task = Content.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('list')
    context = {'task': task}
    return render(request, 'delete.html', context)



