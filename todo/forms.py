from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TasksForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title']


class TasksFormUpdate(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'complete', 'user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
