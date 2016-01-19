import requests
import json

from django.conf import settings

from urlparse import urljoin

from apps.utils.mail import MailSender
from apps.utils.fields import get_fields_and_values, get_changed_fields
from apps.tasks.models import Task, StatusLog
from apps.notifications.models import SlackSetting


class BaseNotifier(object):

    def __init__(self, task, user, fields, updated_fields=None):
        self.task = task
        # self.url = task.project.slack_url
        # self.channel = task.project.slack_channel
        # self.url = "https://hooks.slack.com/services/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"
        # self.channel = "#prj-proman"
        self.user = user
        self.fields = fields
        self.updated_fields = updated_fields

    def notify(self):
        if self.fields['user']:
            self._notify_assigned()

    def update_notify(self):
        if self.fields['user'] and self.updated_fields:
            self._notify_status_change()


class SlackNotifier(BaseNotifier):

    def _notify_assigned(self):
        message = "Task : *%s* \t Status : *Created* \t Assigned to : *%s* " % (
            self.task.title, self.task.user.name)
        self._send(message)

    def _notify_status_change(self):
        message = "Task : *%s* \t Status : *%s* " % (
            self.task.title, self.task.status)
        self._send(message)

    def _send(self, message):
        for ss in self.task.project.slack_settings.all():
            if ss.url and ss.channel and ss.is_active and ss.notify_task:
                sub_url = "#/my-tasks/?task=" + str(self.task.id)
                current_url = urljoin(settings.BASE_URL, sub_url)
                requests.post(
                    ss.url,
                    data=json.dumps({"channel": ss.channel, "username": "Proman", "text": message, 
                        "attachments": [
                            {
                                "fallback": "link to task url",
                                "title": "Click to view details",
                                "title_link": current_url,
                                "color": "good"
                            }
                        ]}))


class MailNotifier(BaseNotifier):

    def _notify_assigned(self):
        self._send('You have been assinged the following task')

    def _notify_status_change(self):
        if 'status' in self.updated_fields and self.fields['status'] == 'rework':
            self._send('Please rework on the following task')
        elif 'title' in self.updated_fields or 'description' in self.updated_fields or 'items' in self.updated_fields:
            self._send('Following task has been updated')
        
    def _send(self, msg):
        if not self.task.user:
            return
        context = {'task': self.task, 'msg': msg}
        self._send_mail(self.task.user, '[Task] ' + self.task.title, 'tasks/email/notify', context)
    
    def _send_mail(self, reciever, subject, template,  context):
        if 'url' not in context.keys():
            context['url'] = settings.BASE_URL
        if not reciever:
            return
        mail = MailSender(reciever)
        mail.compose(subject, template, context)
        mail.send_async()
