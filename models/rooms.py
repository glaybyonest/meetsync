"""Класс Room и функции работы с коллекцией виртуальных комнат (ПР3)."""

from typing import Iterator, List, Optional


class Room:
    """Виртуальная комната (онлайн-зал) для проведения встреч в MeetSync."""

    def __init__(
        self,
        room_id: int,
        name: str,
        capacity: int,
        room_type: str = "Zoom",
        description: str = "",
    ) -> None:
        """Создать объект виртуальной комнаты."""
        if not str(name).strip():
            raise ValueError("Название комнаты не может быть пустым")
        if not self.validate_capacity(capacity):
            raise ValueError("Вместимость должна быть положительным числом")
        self.id: int = int(room_id)
        self.name: str = str(name).strip()
        self.capacity: int = int(capacity)
        self.room_type: str = str(room_type).strip() or "Zoom"
        self.description: str = str(description).strip()

    @staticmethod
    def validate_capacity(capacity: int) -> bool:
        """Проверить корректность значения вместимости."""
        return isinstance(capacity, int) and capacity > 0

    def is_suitable_for(self, people_count: int) -> bool:
        """Проверить, подходит ли онлайн-комната для указанного числа людей."""
        if people_count <= 0:
            return False
        return self.capacity >= people_count

    @property
    def info(self) -> str:
        """Вернуть краткое описание виртуальной комнаты."""
        return f"{self.name} ({self.room_type}, до {self.capacity} мест)"

    def __str__(self) -> str:
        """Вернуть строковое представление виртуальной комнаты."""
        return f"{self.name}, {self.capacity} мест"


def add_room(
    rooms: List[Room],
    name: str,
    capacity: int,
    room_type: str = "Zoom",
    description: str = "",
) -> Room:
    """Создать объект Room, добавить его в коллекцию и вернуть."""
    next_id = max((room.id for room in rooms), default=0) + 1
    room = Room(
        room_id=next_id,
        name=name,
        capacity=capacity,
        room_type=room_type,
        description=description,
    )
    rooms.append(room)
    return room


def find_room_by_id(
    rooms: List[Room],
    room_id: int,
) -> Optional[Room]:
    """Найти объект Room по уникальному идентификатору."""
    for room in rooms:
        if room.id == room_id:
            return room
    return None


def find_room(
    rooms: List[Room],
    query: str,
) -> List[Room]:
    """Найти объекты Room по подстроке названия."""
    needle = query.strip().lower()
    return [room for room in rooms if needle in room.name.lower()]


def check_room_capacity(
    rooms: List[Room],
    room_id: int,
    min_capacity: int,
) -> bool:
    """Найти комнату по ID и проверить её вместимость через метод объекта."""
    room = find_room_by_id(rooms, room_id)
    if room is None:
        return False
    return room.is_suitable_for(min_capacity)


def filter_rooms_by_capacity(
    rooms: List[Room],
    min_capacity: int,
) -> Iterator[Room]:
    """Отобрать объекты Room, подходящие по вместимости."""
    for room in rooms:
        if room.is_suitable_for(min_capacity):
            yield room


def sort_rooms(rooms: List[Room]) -> List[Room]:
    """Отсортировать коллекцию объектов Room по вместимости."""
    return sorted(rooms, key=lambda room: room.capacity)


def show_rooms(rooms: List[Room]) -> None:
    """Вывести список объектов Room в консоль."""
    if not rooms:
        print("Помещения не найдены.")
        return
    for room in rooms:
        print(f"[{room.id}] {room}")
