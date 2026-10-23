#!/usr/bin/env python
"""Утилита командной строки Django для административных задач MeetSync."""
import os
import sys


def main() -> None:
    """Запуск административных задач Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meetsync.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что Django "
            "установлен и активировано виртуальное окружение."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
