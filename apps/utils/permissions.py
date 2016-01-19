import requests

from rest_framework import status
from rest_framework.response import Response


def allow_admin_only(func):
    def admin_check(self, request, *args, **kwargs):
        if request.user.is_superuser == True:
            response = func(self, request, *args, **kwargs)
            return response
        return Response("Sorrryyy......You have no admin rights..!!!!", status=status.HTTP_401_UNAUTHORIZED)
    return admin_check
