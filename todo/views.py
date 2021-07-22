from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def allContent(request):
    all = Content.objects.all()

    form = TasksForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list')
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


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'login.html', context)



