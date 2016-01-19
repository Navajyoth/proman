from django.test import TestCase
from model_mommy import mommy

from apps.projects.models import Project, Milestone, WorkItem
from apps.utils.tests import console_log


class ProjectModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Project)

    def test_project_model(self):
        self.assertTrue(isinstance(self.item, Project))
        console_log('projects', 'model', 'Project')


class MilestoneModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Milestone)

    def test_milestone_model(self):
        self.assertTrue(isinstance(self.item, Milestone))
        console_log('projects', 'model', 'Milestone')


class WorkItemModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(WorkItem)

    def test_workitem_model(self):
        self.assertTrue(isinstance(self.item, WorkItem))
        console_log('projects', 'model', 'WorkItem')
