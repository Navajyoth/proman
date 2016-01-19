from django.conf.urls import patterns, url, include
from rest_framework_nested import routers

from .views import SlackSettingViewSet


router = routers.SimpleRouter()
router.register('slacksettings', SlackSettingViewSet, base_name='slacksettings')

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
