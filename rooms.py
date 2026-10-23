"""Модуль функций для работы с виртуальными комнатами MeetSync (ПР2)."""

from typing import Iterator


def add_room(
    rooms: dict[int, dict],
    room_name: str,
    capacity: int,
) -> None:
    """Добавить виртуальную комнату в словарь rooms."""
    clean_name = room_name.strip()
    if not clean_name:
        raise ValueError("Название комнаты не может быть пустым")
    if capacity <= 0:
        raise ValueError("Вместимость должна быть положительным числом")
    next_id = max(rooms.keys(), default=0) + 1
    rooms[next_id] = {
        "id": next_id,
        "name": clean_name,
        "capacity": capacity,
    }


def find_room(
    rooms: dict[int, dict],
    query: str,
) -> list[dict]:
    """Найти виртуальные комнаты по подстроке названия."""
    needle = query.strip().lower()
    result = []
    for room in rooms.values():
        if needle in room["name"].lower():
            result.append(room)
    return result


def check_room_capacity(
    rooms: dict[int, dict],
    room_id: int,
    min_capacity: int,
) -> bool:
    """Проверить вместимость виртуальной комнаты по идентификатору."""
    room = rooms.get(room_id)
    if room is None or min_capacity <= 0:
        return False
    return room["capacity"] >= min_capacity


def filter_rooms_by_capacity(
    rooms: dict[int, dict],
    min_capacity: int,
) -> Iterator[dict]:
    """Отобрать виртуальные комнаты по минимальной вместимости (генератор)."""
    for room in rooms.values():
        if room["capacity"] >= min_capacity:
            yield room


def sort_rooms(rooms: dict[int, dict]) -> list[dict]:
    """Отсортировать виртуальные комнаты по вместимости (через lambda)."""
    return sorted(rooms.values(), key=lambda item: item["capacity"])
