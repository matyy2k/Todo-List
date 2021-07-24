from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Content(models.Model):
    title = models.CharField(max_length=64)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
