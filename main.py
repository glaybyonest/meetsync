"""Консольное приложение MeetSync на базе объектной модели (ПР3)."""

from typing import List

from models import Booking, Room, User
from models.bookings import (
    cancel_booking,
    create_booking,
    get_booking_status,
    is_room_available,
    show_bookings,
)
from models.rooms import (
    add_room,
    check_room_capacity,
    filter_rooms_by_capacity,
    find_room,
    find_room_by_id,
    show_rooms,
    sort_rooms,
)
from models.users import (
    add_user,
    find_user,
    find_user_by_id,
    show_users,
)
from storage import (
    load_bookings,
    load_rooms,
    load_users,
    save_bookings,
    save_rooms,
    save_users,
)
from utils import input_date, input_int

ROOMS_FILE = "data/rooms.json"
USERS_FILE = "data/users.json"
BOOKINGS_FILE = "data/bookings.json"


def create_new_booking(
    bookings: List[Booking],
    rooms: List[Room],
    users: List[User],
) -> None:
    """Выполнить пользовательский сценарий создания бронирования."""
    room_id = input_int("Введите ID онлайн-комнаты: ")
    room = find_room_by_id(rooms, room_id)
    if room is None:
        print("Онлайн-комната с указанным ID не найдена.")
        return

    user_id = input_int("Введите ID пользователя: ")
    user = find_user_by_id(users, user_id)
    if user is None:
        print("Пользователь с указанным ID не найден.")
        return

    booking_date = input_date("Введите дату встречи (ГГГГ-ММ-ДД): ")
    booking = create_booking(bookings, room, booking_date, user)
    if booking is None:
        print("Онлайн-комната уже занята на выбранную дату.")
        return

    save_bookings(BOOKINGS_FILE, bookings)
    print(f"Создано бронирование #{booking.id}: {booking}")


def main() -> None:
    """Точка входа консольного приложения MeetSync."""
    rooms = load_rooms(ROOMS_FILE)
    users = load_users(USERS_FILE)
    bookings = load_bookings(BOOKINGS_FILE, rooms, users)

    while True:
        print("\n=== MeetSync: Управление онлайн-встречами (ООП) ===")
        print("1. Показать онлайн-комнаты")
        print("2. Найти комнату по названию")
        print("3. Проверить вместимость комнаты")
        print("4. Показать пользователей")
        print("5. Добавить пользователя")
        print("6. Найти пользователя")
        print("7. Проверить доступность комнаты на дату")
        print("8. Создать бронирование онлайн-встречи")
        print("9. Отменить бронирование")
        print("10. Показать все бронирования")
        print("11. Добавить онлайн-комнату")
        print("12. Отбор и сортировка комнат по вместимости")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_rooms(rooms)
        elif choice == "2":
            query = input("Подстрока названия: ")
            show_rooms(find_room(rooms, query))
        elif choice == "3":
            room_id = input_int("ID комнаты: ")
            people = input_int("Количество участников: ")
            ok = check_room_capacity(rooms, room_id, people)
            print("Помещение подходит" if ok else "Мест недостаточно")
        elif choice == "4":
            show_users(users)
        elif choice == "5":
            name = input("Имя пользователя: ")
            email = input("Email пользователя: ")
            add_user(users, name, email)
            save_users(USERS_FILE, users)
            print("Пользователь добавлен.")
        elif choice == "6":
            query = input("Имя или email: ")
            show_users(find_user(users, query))
        elif choice == "7":
            room_id = input_int("ID комнаты: ")
            room = find_room_by_id(rooms, room_id)
            if room is None:
                print("Комната не найдена.")
            else:
                b_date = input_date("Дата (ГГГГ-ММ-ДД): ")
                avail = is_room_available(bookings, room, b_date)
                print(get_booking_status(avail))
        elif choice == "8":
            create_new_booking(bookings, rooms, users)
        elif choice == "9":
            booking_id = input_int("ID бронирования: ")
            if cancel_booking(bookings, booking_id):
                save_bookings(BOOKINGS_FILE, bookings)
                print("Бронирование отменено.")
            else:
                print("Активное бронирование не найдено.")
        elif choice == "10":
            show_bookings(bookings)
        elif choice == "11":
            name = input("Название комнаты: ")
            cap = input_int("Вместимость: ")
            add_room(rooms, name, cap)
            save_rooms(ROOMS_FILE, rooms)
            print("Онлайн-комната добавлена.")
        elif choice == "12":
            min_cap = input_int("Минимальная вместимость: ")
            filtered = list(filter_rooms_by_capacity(rooms, min_cap))
            show_rooms(sort_rooms(filtered))
        elif choice == "0":
            save_rooms(ROOMS_FILE, rooms)
            save_users(USERS_FILE, users)
            save_bookings(BOOKINGS_FILE, bookings)
            print("Работа завершена.")
            break
        else:
            print("Неверная команда.")


if __name__ == "__main__":
    main()
