from rest_framework import serializers
from django.db import transaction

from apps.utils.serializers import JSONSerializerField
from apps.utils.fields import get_fields_and_values, get_changed_fields
from .models import Project, WorkItem, Milestone
from apps.notifications.workitems import SlackNotifier


class ProjectSerializer(serializers.ModelSerializer):
    tags = JSONSerializerField()

    class Meta:
        model = Project
        fields = ('name', 'id', 'owner', 'status', 'is_active', 'tags')


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milestone
        fields = ('name', 'project', 'start_date', 'end_date', 'is_deleted', 'id', 'effort')


class WorkItemSerializer(serializers.ModelSerializer):
    tags = JSONSerializerField()
    notifiers = [SlackNotifier]

    class Meta:
        model = WorkItem
        fields = ('project', 'workitem', 'long_name', 'milestone', 'text', 'status', 'description', 'id', 'effort', 'total_effort', 'sub_effort', 'child_count', 'tags')

    @transaction.atomic
    def update(self, instance, validated_data):
        initial_data = get_fields_and_values(instance)
        item = super(WorkItemSerializer, self).update(instance, validated_data)
        updated_data = get_fields_and_values(item)
        updated_fields = get_changed_fields(initial_data, updated_data)
        [n(item, updated_data, updated_fields).update_notify() for n in self.notifiers]
        return item
