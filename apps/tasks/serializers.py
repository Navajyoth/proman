import json
from django.db import transaction
from rest_framework import serializers

from apps.utils.fields import get_fields_and_values, get_changed_fields
from apps.utils.serializers import JSONSerializerField
from .models import Task, PettyTask, SubTask, StatusLog
from apps.notifications.tasks import SlackNotifier, MailNotifier


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source="project.name", read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)
    notifiers = [MailNotifier, SlackNotifier]
    items = JSONSerializerField()

    class Meta:
        model = Task
        read_only_fields = ('created_by',)
        fields = (
            'id', 'title', 'description', 'user', 'status', 'project', 'project_name',
            'workitem', 'created_by', 'estimated_time', 'user_name', 'actual_time',
            'rework_time', 'tag', 'review_comments', 'reviewer', 'priority',
            'due_date', 'is_overdue', 'items', 'items_completed', 'commits')

    @transaction.atomic
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        item = super(TaskSerializer, self).create(validated_data)
        user = item.user
        fields = get_fields_and_values(item)
        [n(item, user, fields).notify() for n in self.notifiers]
        StatusLog.create_status_log(item)
        return item

    @transaction.atomic
    def update(self, instance, validated_data):
        initial_data = get_fields_and_values(instance)
        item = super(TaskSerializer, self).update(instance, validated_data)
        user = item.user
        updated_data = get_fields_and_values(item)
        updated_fields = get_changed_fields(initial_data, updated_data)
        current_user = self.context['request'].user
        [n(item, user, updated_data, updated_fields).update_notify() for n in self.notifiers]
        return item


class PettyTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = PettyTask
        fields = ("id", "user", "description", "is_completed", "effort", "created_on", "modified_on")


class SubTaskSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super(SubTaskSerializer, self).create(validated_data)

    class Meta:
        model = SubTask
        read_only_fields = ("created_by", "created_on")
        fields = ("id", "task", "text", "is_completed", "kind", "created_by", "created_on")


class TaskMiniSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'user')


class StatusLogSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name')
    task = serializers.CharField(source='task.title')

    class Meta:
        model = StatusLog
        fields = ('id', 'user', 'task', 'status', 'time_stamp')
        read_only_fields = fields
