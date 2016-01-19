import json 

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated

from apps.utils.permissions import allow_admin_only
from .models import Task, PettyTask, SubTask, StatusLog
from .serializers import (
    TaskSerializer, PettyTaskSerializer, SubTaskSerializer,
    TaskMiniSerializer, StatusLogSerializer
)
from .notify import SlackNotifier, MailNotifier


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    # queryset = Task.objects.prefetch_related('commits').all().filter(project__is_active=True)
    queryset = Task.objects.all()

    def list(self, request):
        tasks = self.queryset.filter_by_query_params(request).all()
        detail_str = request.GET.get('detail', True)
        if detail_str:
            slz = TaskSerializer(tasks, many=True)
        else:
            slz = TaskMiniSerializer(tasks, many=True)
        return Response(slz.data)

    @detail_route(methods=['GET'])
    @allow_admin_only
    def notify(self, request, pk=None):
        task = self.get_object()
        data_raw = TaskMiniSerializer(task, many=False)
        data = json.dumps(data_raw.data)
        # task.send_remider_notification()

        # url = "https://hooks.slack.com/services/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"
        # requests.post(url, data = json.dumps({"channel": "#proman", "username": "reenu_bot", "text": data, "icon_emoji": ":smiley:"}))

        return Response('Reminder notification is sent.')

    @list_route(methods=['GET', ])
    def create_from_workitem(self, request):
        workitem = request.GET.get('workitem', None)
        user = request.user.id

        if workitem:
            task = Task.create_from_workitem(workitem, user)
            task = TaskSerializer(task, many=False)
            return Response(task.data)


class PettyTaskViewSet(viewsets.ModelViewSet):
    serializer_class = PettyTaskSerializer
    permission_classes = (IsAuthenticated,)
    queryset = PettyTask.objects.all()


class SubTaskViewSet(viewsets.ModelViewSet):
    serializer_class = SubTaskSerializer
    permission_classes = (IsAuthenticated,)
    queryset = SubTask.objects.all()


class StatusLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StatusLogSerializer
    permission_classes = (IsAuthenticated,)
    queryset = StatusLog.objects.all()
    paginate_by = 10

    def filter_queryset(self, queryset):
        queryset = queryset.filter_by_query_params(self.request)
        return queryset