from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.utils.tests import console_log, BaseViewSetTestMixing
from apps.projects.models import Project, Milestone, WorkItem
from apps.account.models import User


class ProjectsViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "projects"
    model = Project
    app_name = "projects"
   
    def setUp(self):
        self.user = mommy.make(User)
        self.item = mommy.make(Project, owner=self.user)
        self.post_data = {
            'name': 'test proj1',
            'owner': self.user.id,
            'status': 'Green',
            'is_active': True,
            'tags': {}
        }

        self.update_data = {
            'name': 'test proj2',
            'owner': self.user.id,
            'status': 'Green',
            'is_active': True,
            'tags': {}
        }


class MilestoneViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "Milestones"
    model = Milestone
    app_name = "projects"

    def setUp(self):
        self.user = mommy.make(User)
        self.project = mommy.make(Project)
        self.item = mommy.make(Milestone, project=self.project)
        self.post_data = {
            'name': 'test ms1',
            'project': self.project.id
        }

        self.update_data = {
            'name': 'test ms2',
            'project': self.project.id
        }


class WorkItemViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "WorkItems"
    model = WorkItem
    app_name = "projects"

    def setUp(self):
        self.user = mommy.make(User)
        self.project = mommy.make(Project)
        self.milestone = mommy.make(Milestone)
        self.item = mommy.make(WorkItem, project=self.project, milestone=self.milestone)
        self.post_data = {
            'name': 'test workitem1',
            'project': self.project.id,
            'milestone': self.milestone.id,
            'text': 'test text1',
            'status': 'added',
            'effort': 0,
            'sub_effort': 0,
            'total_effort': 0,
            'child_count': 0,
            'tags': {}
        }

        self.update_data = {
            'name': 'test workitem2',
            'project': self.project.id,
            'milestone': self.milestone.id,
            'text': 'test text2',
            'status': 'added',
            'effort': 0,
            'sub_effort': 0,
            'total_effort': 0,
            'child_count': 0,
            'tags': {}
        }
