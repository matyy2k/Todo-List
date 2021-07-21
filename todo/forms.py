from django.forms import ModelForm
from .models import *


class TasksForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'complete']

