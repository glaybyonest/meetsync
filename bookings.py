"""Модуль функций для создания и проверки онлайн-встреч MeetSync (ПР2)."""

from datetime import date
from typing import Optional, Union

DateType = Union[date, str]


def _normalize_date(value: DateType) -> str:
    """Привести дату к строковому формату YYYY-MM-DD."""
    if isinstance(value, date):
        return value.isoformat()
    return str(value).strip()


def is_room_available(
    bookings: list[dict],
    room_id: int,
    booking_date: DateType,
) -> bool:
    """Проверить, свободна ли онлайн-комната на выбранную дату."""
    target_date = _normalize_date(booking_date)
    for booking in bookings:
        same_room = booking["room_id"] == room_id
        same_date = _normalize_date(booking["booking_date"]) == target_date
        if same_room and same_date:
            return False
    return True


def create_booking(
    bookings: list[dict],
    room_id: int,
    booking_date: DateType,
) -> Optional[dict]:
    """Создать новое бронирование онлайн-встречи, если комната свободна."""
    target_date = _normalize_date(booking_date)
    if not is_room_available(bookings, room_id, target_date):
        return None
    next_id = max((b["id"] for b in bookings), default=0) + 1
    new_booking = {
        "id": next_id,
        "room_id": room_id,
        "booking_date": target_date,
    }
    bookings.append(new_booking)
    return new_booking


def cancel_booking(
    bookings: list[dict],
    booking_id: int,
) -> bool:
    """Отменить (удалить) бронирование по идентификатору (этап ПР2)."""
    for index, booking in enumerate(bookings):
        if booking["id"] == booking_id:
            del bookings[index]
            return True
    return False


def get_booking_status(is_available: bool) -> str:
    """Вернуть текстовый статус доступности онлайн-комнаты (из ПР1)."""
    if is_available:
        return "Помещение доступно для бронирования"
    return "Помещение уже занято"
