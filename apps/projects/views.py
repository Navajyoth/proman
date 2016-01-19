import json
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route

from .models import Project, WorkItem, Milestone
from .serializers import ProjectSerializer, WorkItemSerializer, MilestoneSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.active()

    @list_route(methods=['GET', ])
    def summary(self, request):
        result = []
        for project in self.queryset.all():
            status_list = list(project.tasks.values_list('status', flat=True))
            data = {
                'id': project.id,
                'name': project.name,
                'status': project.status,
            }
            for status in status_list:
                data[status] = status_list.count(status)
            result.append(data)
        return Response(result)


class MilestoneViewSet(viewsets.ModelViewSet):
    serializer_class = MilestoneSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Milestone.objects.all()

    def get_queryset(self):
        queryset = Milestone.objects.all()
        project_query = self.request.query_params.get('project', None)
        if project_query is not None:
            queryset = queryset.filter(project=int(project_query))
        return queryset


class WorkItemViewSet(viewsets.ModelViewSet):
    serializer_class = WorkItemSerializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkItem.objects.all()

    def get_queryset(self):
        queryset = WorkItem.objects.all()
        project_query = self.request.query_params.get('project', None)
        text_query = self.request.query_params.get('text', None)
        if project_query is not None:
            queryset = queryset.filter(project=int(project_query))
        if text_query is not None:
            queryset = queryset.filter(text=text_query)
        return queryset
