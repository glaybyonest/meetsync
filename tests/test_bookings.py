"""Тесты класса Booking и правил доступности онлайн-комнат (ПР3)."""

from models import Booking, Room, User
from models.bookings import (
    cancel_booking,
    create_booking,
    find_booking_by_id,
    get_booking_status,
    is_room_available,
)


def test_booking_creation() -> None:
    """Проверить создание объекта Booking и ссылки на Room и User."""
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван Петров", "ivan@example.com")
    booking = Booking(1, room, "2026-09-15", user)
    assert booking.id == 1
    assert booking.room is room
    assert booking.user is user
    assert booking.booking_date == "2026-09-15"
    assert not booking.is_cancelled


def test_booking_cancel() -> None:
    """Проверить отмену бронирования методом cancel()."""
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван Петров", "ivan@example.com")
    booking = Booking(1, room, "2026-09-15", user)
    booking.cancel()
    assert booking.is_cancelled
    assert "отменено" in str(booking)


def test_room_availability_and_rebooking_after_cancel() -> None:
    """Проверить блокировку комнаты и повторную бронь после отмены."""
    room = Room(1, "Аудитория 301", 30)
    user_1 = User(1, "Иван Петров", "ivan@example.com")
    user_2 = User(2, "Анна Смирнова", "anna@example.com")
    bookings: list[Booking] = []

    booking_1 = create_booking(bookings, room, "2026-09-15", user_1)
    assert booking_1 is not None
    assert not is_room_available(bookings, room, "2026-09-15")

    duplicate = create_booking(bookings, room, "2026-09-15", user_2)
    assert duplicate is None

    assert cancel_booking(bookings, booking_1.id)
    assert booking_1 in bookings
    assert booking_1.is_cancelled
    assert is_room_available(bookings, room, "2026-09-15")

    booking_2 = create_booking(bookings, room, "2026-09-15", user_2)
    assert booking_2 is not None
    assert find_booking_by_id(bookings, booking_2.id) is booking_2
    assert get_booking_status(True) == "Помещение доступно для бронирования"
