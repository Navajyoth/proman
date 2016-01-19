from django.db import models
from django.db.models import Q


class TaskQuerySet(models.QuerySet):

    def active(self):
        items = self.exclude(status__in=('cancel', 'archive'))
        return items

    def filter_by_query_params(self, request):
        term = request.GET.get('term', None)
        status = request.GET.get('status', None)
        exclude = request.GET.get('exclude', None)
        project_id = request.GET.get('project', None)
        user_id = request.GET.get('user', None)
        current_user = request.GET.get('current')
        items = self

        if current_user:
            items = items.filter(user=request.user)
        if term:
            items = items.filter(Q(title__icontains=term) | Q(description__icontains=term))
        if status:
            status_list = [s for s in status.split(',')]
            items = items.filter(status__in=status_list)
        if exclude:
            exclude_list = [e for e in exclude.split(',')]
            items = items.exclude(status__in=exclude_list)

        if project_id:
            items = items.filter(project=int(project_id))
        if user_id:
            items = items.filter(user=int(user_id))

        return items


class StatusLogQuerySet(models.QuerySet):
    
    def filter_by_query_params(self, request):
        task_id = request.GET.get('task', None)
        user_id = request.GET.get('user', None)
        items = self

        if task_id:
            items = items.filter(task=int(task_id))
        elif user_id:
            items = items.filter(user=int(user_id))
        return items

