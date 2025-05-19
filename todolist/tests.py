from django.test import TestCase, Client
from django.urls import reverse
from .models import Task
from django.utils import timezone

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title="Test Task", completed=False)

    def test_add_task(self):
        response = self.client.post(reverse('add_task'), {
            'title': 'New Task',
            'date': '2025-05-20',
            'time': '14:30'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(title="New Task").exists())

    def test_toggle_task(self):
        response = self.client.get(reverse('toggle_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        response = self.client.get(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())