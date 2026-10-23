"""Класс Booking и функции управления бронированиями онлайн-встреч (ПР3)."""

from datetime import date
from typing import List, Optional, Union

from .rooms import Room
from .users import User

DateType = Union[date, str]


def _normalize_date(value: DateType) -> str:
    """Привести дату бронирования к строке формата YYYY-MM-DD."""
    if isinstance(value, date):
        return value.isoformat()
    return str(value).strip()


class Booking:
    """Бронирование виртуальной комнаты пользователем на выбранную дату."""

    def __init__(
        self,
        booking_id: int,
        room: Room,
        booking_date: DateType,
        user: User,
        is_cancelled: bool = False,
    ) -> None:
        """Создать объект бронирования с объектами Room и User."""
        self.id: int = int(booking_id)
        self.room: Room = room
        self.booking_date: str = _normalize_date(booking_date)
        self.user: User = user
        self.is_cancelled: bool = bool(is_cancelled)

    def cancel(self) -> None:
        """Отменить бронирование (изменить состояние без удаления объекта)."""
        self.is_cancelled = True

    def __str__(self) -> str:
        """Вернуть строковое представление бронирования с учётом статуса."""
        status = "отменено" if self.is_cancelled else "активно"
        return (
            f"Бронирование #{self.id}: {self.room.name}, "
            f"дата {self.booking_date}, пользователь {self.user.name} "
            f"({status})"
        )


def find_booking_by_id(
    bookings: List[Booking],
    booking_id: int,
) -> Optional[Booking]:
    """Найти объект Booking по идентификатору."""
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    return None


def is_room_available(
    bookings: List[Booking],
    room: Room,
    booking_date: DateType,
) -> bool:
    """Проверить доступность объекта Room с учётом активных бронирований."""
    target_date = _normalize_date(booking_date)
    for booking in bookings:
        same_room = booking.room.id == room.id
        same_date = booking.booking_date == target_date
        if same_room and same_date and not booking.is_cancelled:
            return False
    return True


def create_booking(
    bookings: List[Booking],
    room: Room,
    booking_date: DateType,
    user: User,
) -> Optional[Booking]:
    """Проверить доступность, создать объект Booking и добавить в список."""
    target_date = _normalize_date(booking_date)
    if not is_room_available(bookings, room, target_date):
        return None
    next_id = max((b.id for b in bookings), default=0) + 1
    booking = Booking(
        booking_id=next_id,
        room=room,
        booking_date=target_date,
        user=user,
    )
    bookings.append(booking)
    return booking


def cancel_booking(
    bookings: List[Booking],
    booking_id: int,
) -> bool:
    """Найти бронирование по ID и вызвать его метод cancel()."""
    booking = find_booking_by_id(bookings, booking_id)
    if booking is None or booking.is_cancelled:
        return False
    booking.cancel()
    return True


def get_booking_status(is_available: bool) -> str:
    """Сформировать текстовое сообщение о доступности онлайн-комнаты."""
    if is_available:
        return "Помещение доступно для бронирования"
    return "Помещение уже занято"


def show_bookings(bookings: List[Booking]) -> None:
    """Вывести список всех объектов Booking в консоль."""
    if not bookings:
        print("Бронирования не найдены.")
        return
    for booking in bookings:
        print(booking)
