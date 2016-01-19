import json
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route

from .models import SlackSetting
from .serializers import SlackSettingSerializer


class SlackSettingViewSet(viewsets.ModelViewSet):
    serializer_class = SlackSettingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = SlackSetting.objects.all()
