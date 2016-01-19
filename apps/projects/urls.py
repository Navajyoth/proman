from django.conf.urls import patterns, url, include
from rest_framework_nested import routers

from .views import ProjectViewSet, WorkItemViewSet, MilestoneViewSet


router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, base_name='projects')
router.register('workitems', WorkItemViewSet, base_name='WorkItems')
router.register('milestones', MilestoneViewSet, base_name='Milestones')


urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
