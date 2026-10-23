"""Представления приложения homepage на основе шаблонов Django (ПР6)."""
from django.shortcuts import render


def index(request):
    """Отобразить главную страницу сервиса MeetSync."""
    return render(
        request,
        "homepage/index.html",
    )


def page_not_found(request, exception):
    """Отобразить пользовательскую страницу ошибки 404."""
    return render(
        request,
        "homepage/404.html",
        status=404,
    )
