import json
from django.db import transaction
from rest_framework import serializers

from apps.utils.serializers import JSONSerializerField
from .models import SlackSetting


class SlackSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlackSetting
        fields = ("channel", "url", "is_active", "notify_task", "notify_workitem", "project")
