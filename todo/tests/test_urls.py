from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import update_tasks, delete_tasks, all_content


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, all_content)

    def test_update_url_is_resolved(self):
        url = reverse('update', args=[4])
        self.assertEqual(resolve(url).func, update_tasks)

    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=[1])
        self.assertEqual(resolve(url).func, delete_tasks)