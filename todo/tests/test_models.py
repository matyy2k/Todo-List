import datetime

from django.test import TestCase
from todo.models import Content
from unittest.mock import patch, Mock


class TestModels(TestCase):

    def setUp(self):
        self.test = Content.objects.create(title='test1', complete=True, created=True)

    def test_title_label(self):
        title = Content.objects.get(id=1)
        field_label = title._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        title = Content.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEqual(max_length, 64)

    def test_str_is_equal_title(self):
        title = Content.objects.get(id=1)
        self.assertEqual(str(title), self.test.title)

    @patch('django.utils.timezone.now', )
    def test_something(self, mock_now):
        mocked_dt = datetime.datetime(2015, 9, 3, 11, 15, 0)
        with patch('django.utils.timezone.now', Mock(return_value=mocked_dt)):
            my_obj = Content.objects.create().created
            expected = datetime.datetime(2015, 9, 3, 11, 15) # do poprawy
            self.assertEqual(my_obj, expected)

