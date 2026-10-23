"""Представления (view-функции) приложения bookings (ПР5)."""
from django.http import HttpResponse

from homepage.views import page
from models.bookings import find_booking_by_id
from storage import load_bookings, load_rooms, load_users


def bookings(request):
    """Отобразить список онлайн-встреч (бронирований) из JSON."""
    rooms_list = load_rooms("data/rooms.json")
    users_list = load_users("data/users.json")
    bookings_list = load_bookings(
        "data/bookings.json",
        rooms_list,
        users_list,
    )

    items = ""
    for booking in bookings_list:
        status = "отменено" if booking.is_cancelled else "активно"
        badge = (
            "bg-secondary" if booking.is_cancelled else "bg-success"
        )
        items += f"""
        <li class="list-group-item d-flex justify-content-between">
            <a href="/bookings/{booking.id}/">
                {booking.room.name} – {booking.booking_date}
            </a>
            <span class="badge {badge}">
                {status}
            </span>
        </li>
        """
    content = f"""
    <h1>Онлайн-встречи (бронирования)</h1>
    <ul class="list-group">
        {items}
    </ul>
    """
    return HttpResponse(
        page("MeetSync – бронирования", content)
    )


def booking_detail(request, booking_id: int):
    """Отобразить страницу конкретной онлайн-встречи по ID."""
    rooms_list = load_rooms("data/rooms.json")
    users_list = load_users("data/users.json")
    bookings_list = load_bookings(
        "data/bookings.json",
        rooms_list,
        users_list,
    )
    booking = find_booking_by_id(
        bookings_list,
        booking_id,
    )
    if booking is None:
        content = """
        <h1 class="text-danger">
            Бронирование не найдено
        </h1>
        <a href="/bookings/"
           class="btn btn-outline-secondary">
            ← к списку бронирований
        </a>
        """
        return HttpResponse(
            page("Бронирование не найдено", content),
            status=404,
        )

    status = "отменено" if booking.is_cancelled else "активно"
    badge = "bg-secondary" if booking.is_cancelled else "bg-success"
    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">
                Бронирование №{booking.id}
            </h5>
            <p class="card-text">
                Онлайн-комната: {booking.room.name}
            </p>
            <p class="card-text">
                Дата: {booking.booking_date}
            </p>
            <p class="card-text">
                Организатор: {booking.user.name} ({booking.user.email})
            </p>
            <p class="card-text">
                Статус:
                <span class="badge {badge}">
                    {status}
                </span>
            </p>
            <a href="/bookings/"
               class="btn btn-outline-secondary">
                ← к списку бронирований
            </a>
        </div>
    </div>
    """
    return HttpResponse(
        page(
            f"Бронирование №{booking.id}",
            content,
        ),
        status=200,
    )
