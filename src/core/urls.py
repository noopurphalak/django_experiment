from django.urls import path

from . import api

app_name = "core"

urlpatterns = [
    path("api/core/dummy-api-1/", api.DummyAPI1.as_view(), name="dummy_api_1"),
    path("api/core/dummy-api-2/", api.DummyAPI2.as_view(), name="dummy_api_2"),
]
