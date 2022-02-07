from django.test import TestCase
from todo.forms import *


class TestForms(TestCase):
    def test_empty_form(self):
        form = TasksForm()
        self.assertIn('title', form.fields)

    def test_form_valid_data(self):
        form = TasksForm(data={
            'title': 'tytul'
        })
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = TasksForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)