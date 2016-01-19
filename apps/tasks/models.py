import json
from django.utils import timezone
from django.db import models
from django.conf import settings

from model_utils.fields import StatusField
from model_utils import Choices
from jsonfield import JSONField

from apps.utils.models import AbstractTimestampModel
from apps.projects.models import Project, WorkItem
from apps.account.models import User
from apps.core.models import WorkType, Technology
from apps.utils.mail import MailSender
from .managers import TaskQuerySet, StatusLogQuerySet


class Task(AbstractTimestampModel):
    STATUS = Choices('backlog', 'progress', 'rework', 'review', 'complete', 'cancel', 'archive')

    title = models.CharField(max_length=256)
    project = models.ForeignKey(Project, related_name='tasks')
    workitem = models.ForeignKey(WorkItem, related_name='tasks', null=True, blank=True)

    user = models.ForeignKey(User, related_name='tasks', null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_tasks')
    description = models.CharField(max_length=2048, null=True, blank=True)
    status = StatusField(default=STATUS.backlog)
    priority = models.CharField(max_length=16, default='normal')
    due_date = models.DateTimeField(null=True, blank=True)

    estimated_time = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    actual_time = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    rework_time = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    tag = models.CharField(max_length=128, null=True, blank=True)
    review_comments = models.CharField(max_length=1024, null=True, blank=True)
    reviewer = models.ForeignKey(User, related_name='reviews', null=True, blank=True)
    items = JSONField(null=True, blank=True)
    commits = JSONField(null=True, blank=True)

    objects = TaskQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    @property
    def is_overdue(self):
        if not self.due_date:
            return False
        if self.status not in [Task.STATUS.backlog, Task.STATUS.progress, Task.STATUS.rework]:
            return False
        return self.due_date < timezone.now()

    @property
    def items_completed(self):

        if not self.items:
            return []
        complete = [i for i in self.items if bool(i['completed']) == True]
        return complete     

    @classmethod
    def create_from_workitem(cls, workitem_id, user_id):
        workitem = WorkItem.objects.get(pk=workitem_id)
        user = User.objects.get(pk=user_id)
        
        task = Task.objects.create(
            title=workitem.long_name,
            workitem=workitem,
            project=workitem.project,
            created_by=user)
        return task

    class Meta:
        ordering = ('due_date',)


class PettyTask(AbstractTimestampModel):
    user = models.ForeignKey(User, null=True, blank=True, related_name='petty_task')
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    effort = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ('user', 'id')


class SubTask(models.Model):
    KIND = Choices("task", "review", "blog")

    task = models.ForeignKey(Task, related_name='sub_tasks')
    text = models.CharField(max_length=512)
    is_completed = models.BooleanField(default=False)
    kind = StatusField(choices_name="KIND", default=KIND.task)
    created_by = models.ForeignKey(User, related_name='sub_tasks')
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.task.title, self.text)


class StatusLog(models.Model):
    task = models.ForeignKey(Task, related_name='status_logs')
    user = models.ForeignKey(User, related_name='status_logs', null=True, blank=True)
    status = models.CharField(max_length=16)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s(%s) - %s" % (self.task.title, self.status, self.time_stamp)

    objects = StatusLogQuerySet.as_manager()

    class Meta:
        ordering = ('-pk',)

    @classmethod
    def create_status_log(cls, task):
        if task.user:
            user = task.user
        else:
            user = task.project.owner
        StatusLog.objects.create(task=task, status=task.status, user=task.user)
