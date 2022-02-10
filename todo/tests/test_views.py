from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from todo.models import Content
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Content.objects.create(
            title='tytul'
        )

    def test_project_list_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo.html')
        # self.assertEqual()

    def test_add_new_task_post_method(self):
        response = self.client.post(self.list_url, {
            'title': 'tutul'
        })

        self.assertEqual(response.status_code, 302)