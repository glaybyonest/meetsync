"""Вспомогательные функции безопасного пользовательского ввода (ПР2)."""

from datetime import date


def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число с защитой от ошибок."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: введите корректное целое число.")


def input_date(prompt: str) -> str:
    """Запросить у пользователя дату в формате YYYY-MM-DD."""
    while True:
        raw = input(prompt).strip()
        try:
            parsed = date.fromisoformat(raw)
            return parsed.isoformat()
        except ValueError:
            print("Ошибка: введите дату в формате ГГГГ-ММ-ДД.")
