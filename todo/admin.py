from django.contrib import admin
from .models import *


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete', 'created']