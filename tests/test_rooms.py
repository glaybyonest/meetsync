"""Тесты класса Room и функций работы с комнатами (ПР3)."""

from models import Room
from models.rooms import (
    add_room,
    check_room_capacity,
    filter_rooms_by_capacity,
    find_room,
    find_room_by_id,
    sort_rooms,
)


def test_room_creation() -> None:
    """Проверить создание объекта Room и его атрибуты."""
    room = Room(1, "Аудитория 301", 30)
    assert room.id == 1
    assert room.name == "Аудитория 301"
    assert room.capacity == 30
    assert str(room) == "Аудитория 301, 30 мест"
    assert "Аудитория 301" in room.info


def test_room_is_suitable_for() -> None:
    """Проверить метод экземпляра is_suitable_for() и валидацию."""
    room = Room(1, "Аудитория 301", 30)
    assert room.is_suitable_for(20)
    assert room.is_suitable_for(30)
    assert not room.is_suitable_for(40)
    assert Room.validate_capacity(30)
    assert not Room.validate_capacity(0)


def test_room_collection_functions() -> None:
    """Проверить добавление, поиск, фильтрацию и сортировку объектов Room."""
    rooms: list[Room] = []
    add_room(rooms, "Конференц-зал", 60)
    add_room(rooms, "Аудитория 301", 30)
    assert len(rooms) == 2
    assert find_room_by_id(rooms, 1) is rooms[0]
    assert len(find_room(rooms, "аудитория")) == 1
    assert check_room_capacity(rooms, 1, 50)
    assert not check_room_capacity(rooms, 2, 50)
    filtered = list(filter_rooms_by_capacity(rooms, 40))
    assert len(filtered) == 1
    ordered = sort_rooms(rooms)
    assert [r.capacity for r in ordered] == [30, 60]
