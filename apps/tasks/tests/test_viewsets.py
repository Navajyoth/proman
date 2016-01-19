import json

from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.utils.tests import console_log, BaseViewSetTestMixing
from apps.projects.models import Project, WorkItem
from apps.tasks.models import Task
from apps.account.models import User


class TaskViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "tasks"
    model = Task
    app_name = "tasks"

    def setUp(self):
        self.user = mommy.make(User)
        self.project = mommy.make(Project)
        self.workitem = mommy.make(WorkItem)

        self.item = mommy.make(Task, project=self.project, workitem=self.workitem)
        self.post_data = {
            'title': 'Test Task',
            'description': 'Test Task1',
            'user': self.user.id,
            'status': 'backlog',
            'project': self.project.id,
            'project_name': self.project.name,
            'workitem': self.workitem.id,
            'user_name': self.user.name,
            'created_by': self.user.id,
            'priority': 'normal',
            'commits': {},
            'items': {}
        }

        self.update_data = {
            'title': 'Test Task',
            'description': 'Test Task2',
            'user': self.user.id,
            'status': 'backlog',
            'project': self.project.id,
            'project_name': self.project.name,
            'workitem': self.workitem.id,
            'user_name': self.user.name,
            'created_by': self.user.id,
            'priority': 'normal',
            'commits': {},
            'items': {}
        }
