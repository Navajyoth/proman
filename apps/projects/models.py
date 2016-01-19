from model_utils.fields import StatusField
from model_utils import Choices
from django.utils import timezone
from jsonfield import JSONField

from django.db import models
from apps.core.models import WorkType
from apps.account.models import User
from .managers import ProjectQuerySet


class Project(models.Model):
    STATUS = Choices('Green', 'Yellow', 'Red')

    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, null=True, blank=True)
    status = StatusField(default=STATUS.Green)
    is_active = models.BooleanField(default=True)
    tags = JSONField(null=True, blank=True)

    objects = ProjectQuerySet.as_manager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Milestone(models.Model):
    name = models.CharField(max_length=64)
    project = models.ForeignKey(Project, related_name="milestones")
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    @property
    def effort(self):
        effort = sum([i.total_effort for i in self.workitems.all()])
        return effort


class WorkItem(models.Model):
    STATUS = Choices('added', 'progress', 'completed', 'tested', 'issue', 'deleted')

    project = models.ForeignKey(Project, related_name="workitems")
    workitem = models.ForeignKey('self', related_name="subitems", null=True, blank=True)
    text = models.CharField(max_length=512)
    status = StatusField(default=STATUS.added)
    effort = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=2048, null=True, blank=True)
    tags = JSONField(null=True, blank=True)
    milestone = models.ForeignKey(Milestone, related_name="workitems", null=True, blank=True)

    @property
    def sub_effort(self):
        sub_effort = sum([i.total_effort for i in self.subitems.all()])
        return sub_effort

    @property
    def total_effort(self):
        if self.child_count:
            return self.sub_effort
        return self.effort

    @property
    def child_count(self):
        return self.subitems.count()

    @property
    def long_name(self):
        workitem = self.workitem
        text = []
        while workitem:
            text.append(str(workitem.text))
            workitem = workitem.workitem
        text = ' > '.join(text)
        return text
