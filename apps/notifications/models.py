from django.db import models

from apps.projects.models import Project

class SlackSetting(models.Model):
    channel = models.CharField(max_length=64, null=True, blank=True)
    url = models.URLField(max_length=512, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    notify_task = models.BooleanField()
    notify_workitem = models.BooleanField()
    project = models.ForeignKey(Project, related_name="slack_settings")

    def __unicode__(self):
        return self.channel
