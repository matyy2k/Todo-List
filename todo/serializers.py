from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Content


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'complete', 'created']

