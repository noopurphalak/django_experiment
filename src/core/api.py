import time

from rest_framework import views
from rest_framework.response import Response


class DummyAPI1(views.APIView):
    def get(self, request):
        time.sleep(20)
        return Response({"message": "This is a dummy API 1 response."})


class DummyAPI2(views.APIView):
    def get(self, request):
        time.sleep(5)
        return Response({"message": "This is a dummy API 2 response."})
