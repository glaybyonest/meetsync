"""Конфигурация приложения bookings."""
from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """Класс конфигурации приложения bookings."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "bookings"
