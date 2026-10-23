"""Автоматические тесты функций бронирования онлайн-встреч (ПР2)."""

from datetime import date

from bookings import (
    cancel_booking,
    create_booking,
    get_booking_status,
    is_room_available,
)


def test_is_room_available() -> None:
    """Проверить доступность свободной комнаты на дату."""
    bookings: list[dict] = []
    assert is_room_available(bookings, 1, date(2026, 9, 15))


def test_duplicate_booking_forbidden() -> None:
    """Проверить запрет повторного бронирования комнаты на ту же дату."""
    bookings: list[dict] = []
    created = create_booking(bookings, 1, date(2026, 9, 15))
    assert created is not None
    assert not is_room_available(bookings, 1, date(2026, 9, 15))
    duplicate = create_booking(bookings, 1, date(2026, 9, 15))
    assert duplicate is None


def test_cancel_booking_and_status() -> None:
    """Проверить отмену бронирования и текстовый статус."""
    bookings: list[dict] = []
    created = create_booking(bookings, 1, "2026-09-20")
    assert created is not None
    assert cancel_booking(bookings, created["id"])
    assert is_room_available(bookings, 1, "2026-09-20")
    assert get_booking_status(True) == "Помещение доступно для бронирования"
    assert get_booking_status(False) == "Помещение уже занято"
