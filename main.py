"""Начальный сценарий сервиса управления онлайн-встречами MeetSync (ПР1)."""

from datetime import date


def get_booking_status(is_available: bool) -> str:
    """Вернуть текстовый статус доступности онлайн-комнаты."""
    if is_available:
        return "Онлайн-комната доступна для бронирования встречи"
    return "Онлайн-комната уже занята"


def check_room_capacity(capacity: int, participants: int) -> bool:
    """Проверить, вмещает ли виртуальная комната всех участников встречи."""
    if capacity <= 0 or participants <= 0:
        return False
    return capacity >= participants


def format_meeting_info(
    room_name: str,
    capacity: int,
    meeting_date: date,
    participants: int,
    is_available: bool,
) -> str:
    """Сформировать сводную информацию об онлайн-встрече."""
    status_text = get_booking_status(is_available)
    fits = check_room_capacity(capacity, participants)
    if is_available and fits:
        verdict = "Встреча может быть проведена"
    elif not is_available:
        verdict = "Отклонено: слот занят другой встречей"
    else:
        verdict = "Отклонено: превышен лимит участников онлайн-комнаты"
    return (
        f"Онлайн-комната: {room_name}\n"
        f"Лимит участников: {capacity} человек\n"
        f"Заявлено участников: {participants} человек\n"
        f"Дата встречи: {meeting_date}\n"
        f"Статус слота: {status_text}\n"
        f"Итог проверки: {verdict}"
    )


if __name__ == "__main__":
    room_name = "Зал стратегических сессий Zoom-1"
    capacity = int("30")
    participants = int("18")
    booking_date = date(2026, 9, 15)
    is_available = True

    report = format_meeting_info(
        room_name=room_name,
        capacity=capacity,
        meeting_date=booking_date,
        participants=participants,
        is_available=is_available,
    )
    print(report)
