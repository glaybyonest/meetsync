"""Модуль сохранения и загрузки данных в формате JSON (ПР2)."""

import json


def load_rooms(filename: str = "data/rooms.json") -> dict[int, dict]:
    """Загрузить виртуальные комнаты из JSON-файла в словарь по id."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            raw_list = json.load(file)
            return {int(item["id"]): item for item in raw_list}
    except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
        return {}


def save_rooms(
    filename: str,
    rooms: dict[int, dict],
) -> None:
    """Сохранить словарь виртуальных комнат в JSON-файл."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            list(rooms.values()),
            file,
            ensure_ascii=False,
            indent=2,
        )


def load_bookings(filename: str = "data/bookings.json") -> list[dict]:
    """Загрузить список бронирований онлайн-встреч из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return list(data) if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_bookings(
    filename: str,
    bookings: list[dict],
) -> None:
    """Сохранить список бронирований онлайн-встреч в JSON-файл."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(bookings, file, ensure_ascii=False, indent=2)
