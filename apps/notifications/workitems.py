import requests
import json

from django.conf import settings

from apps.utils.mail import MailSender
from apps.utils.fields import get_fields_and_values, get_changed_fields
from apps.tasks.models import Task, StatusLog
from apps.notifications.models import SlackSetting


class BaseNotifier(object):

    def __init__(self, workitem, fields, updated_fields=None):
        self.workitem = workitem
        self.fields = fields
        self.updated_fields = updated_fields

    def update_notify(self):
        if 'status' in self.updated_fields:
            self._notify_status_change()


class SlackNotifier(BaseNotifier):

    def _notify_status_change(self):
        message = "WI : *%s* \t Status : *%s*" % (
            self.workitem.long_name, self.workitem.status)
        self._send(message)

    def _send(self, message):
        for ss in self.workitem.project.slack_settings.all():
            if ss.url and ss.channel and ss.is_active and ss.notify_workitem:
                requests.post(
                    ss.url,
                    data=json.dumps({"channel": ss.channel, "username": "Proman", "text": message})
                    )
