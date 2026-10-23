"""Автоматические тесты функций работы с онлайн-комнатами (ПР2)."""

from rooms import (
    add_room,
    check_room_capacity,
    filter_rooms_by_capacity,
    find_room,
    sort_rooms,
)


def test_add_room() -> None:
    """Проверить добавление онлайн-комнаты в словарь."""
    rooms: dict[int, dict] = {}
    add_room(rooms, "Аудитория 301", 30)
    assert len(rooms) == 1
    assert rooms[1]["name"] == "Аудитория 301"
    assert rooms[1]["capacity"] == 30


def test_find_room() -> None:
    """Проверить поиск онлайн-комнаты по подстроке названия."""
    rooms: dict[int, dict] = {}
    add_room(rooms, "Аудитория 301", 30)
    add_room(rooms, "Конференц-зал", 60)
    found = find_room(rooms, "аудитория")
    assert len(found) == 1
    assert found[0]["id"] == 1


def test_check_room_capacity() -> None:
    """Проверить соответствие комнаты требуемой вместимости."""
    rooms: dict[int, dict] = {}
    add_room(rooms, "Конференц-зал", 60)
    assert check_room_capacity(rooms, 1, 50)
    assert not check_room_capacity(rooms, 1, 80)


def test_filter_and_sort_rooms() -> None:
    """Проверить генератор фильтрации и сортировку комнат."""
    rooms: dict[int, dict] = {}
    add_room(rooms, "Зал А", 60)
    add_room(rooms, "Зал Б", 15)
    add_room(rooms, "Зал В", 30)
    filtered = list(filter_rooms_by_capacity(rooms, 25))
    assert len(filtered) == 2
    ordered = sort_rooms(rooms)
    assert [r["capacity"] for r in ordered] == [15, 30, 60]
