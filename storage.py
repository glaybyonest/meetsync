"""Модуль преобразования данных JSON <-> объекты Room, User, Booking (ПР3)."""

import json
from typing import List

from models import Booking, Room, User
from models.rooms import find_room_by_id
from models.users import find_user_by_id


def load_rooms(filename: str = "data/rooms.json") -> List[Room]:
    """Загрузить виртуальные комнаты из JSON и создать список объектов Room."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    rooms: List[Room] = []
    for item in raw_data:
        rooms.append(
            Room(
                room_id=item["id"],
                name=item["name"],
                capacity=item["capacity"],
                room_type=item.get("room_type", "Zoom"),
                description=item.get("description", ""),
            )
        )
    return rooms


def save_rooms(filename: str, rooms: List[Room]) -> None:
    """Сохранить коллекцию объектов Room в JSON-файл."""
    payload = [
        {
            "id": room.id,
            "name": room.name,
            "capacity": room.capacity,
            "room_type": room.room_type,
            "description": room.description,
        }
        for room in rooms
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)


def load_users(filename: str = "data/users.json") -> List[User]:
    """Загрузить пользователей из JSON и создать список объектов User."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return [User.from_data(item) for item in raw_data]


def save_users(filename: str, users: List[User]) -> None:
    """Сохранить коллекцию объектов User в JSON-файл."""
    payload = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        }
        for user in users
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)


def load_bookings(
    filename: str = "data/bookings.json",
    rooms: List[Room] | None = None,
    users: List[User] | None = None,
) -> List[Booking]:
    """Загрузить бронирования из JSON и связать их с объектами Room и User."""
    if rooms is None:
        rooms = load_rooms()
    if users is None:
        users = load_users()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    bookings: List[Booking] = []
    for item in raw_data:
        room = find_room_by_id(rooms, item["room_id"])
        user = find_user_by_id(users, item["user_id"])
        if room is None or user is None:
            continue
        booking = Booking(
            booking_id=item["id"],
            room=room,
            booking_date=item["booking_date"],
            user=user,
            is_cancelled=bool(item.get("is_cancelled", False)),
        )
        bookings.append(booking)
    return bookings


def save_bookings(filename: str, bookings: List[Booking]) -> None:
    """Сохранить коллекцию объектов Booking в JSON-файл."""
    payload = [
        {
            "id": booking.id,
            "room_id": booking.room.id,
            "booking_date": booking.booking_date,
            "user_id": booking.user.id,
            "is_cancelled": booking.is_cancelled,
        }
        for booking in bookings
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)
