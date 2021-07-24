from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {user}')
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                messages.info(request, 'Username or password incorrect')
        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def allContent(request):
    all = Content.objects.filter(user=request.user)

    form = TasksForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('list')
    context = {'tasks': all, 'form': form}
    return render(request, 'todo.html', context)


@login_required(login_url='login')
def updateTasks(request, pk):
    task = Content.objects.get(id=pk)

    form = TasksFormUpdate(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('list')

    context = {'form': form}
    return render(request, 'update.html', context)

@login_required(login_url='login')
def deleteTasks(request, pk):
    task = Content.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('list')
    context = {'task': task}
    return render(request, 'delete.html', context)





