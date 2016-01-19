from django.test import TestCase

from model_mommy import mommy

from apps.tasks.models import Task
from apps.utils.tests import console_log


class TaskModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Task)

    def test_task_model(self):
        self.assertTrue(isinstance(self.item, Task))
        console_log('tasks', 'model', 'Task')
