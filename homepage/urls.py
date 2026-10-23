"""Маршруты приложения homepage с пространством имён."""
from django.urls import path

from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.index, name="index"),
]
