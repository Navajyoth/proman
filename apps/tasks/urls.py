from django.conf.urls import patterns, url, include
from rest_framework_nested import routers

from .views import TaskViewSet, PettyTaskViewSet, SubTaskViewSet, StatusLogViewSet

router = routers.SimpleRouter()
router.register('tasks', TaskViewSet, base_name='tasks')
router.register('petty-tasks', PettyTaskViewSet, base_name='petty-tasks')
router.register('sub-tasks', SubTaskViewSet, base_name='sub-tasks')
router.register('status-logs', StatusLogViewSet, base_name='status-logs')

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
