"""Точка запуска консольного приложения MeetSync (ПР2)."""

from bookings import (
    cancel_booking,
    create_booking,
    get_booking_status,
    is_room_available,
)
from rooms import (
    add_room,
    check_room_capacity,
    filter_rooms_by_capacity,
    find_room,
    sort_rooms,
)
from storage import (
    load_bookings,
    load_rooms,
    save_bookings,
    save_rooms,
)
from utils import input_date, input_int

ROOMS_FILE = "data/rooms.json"
BOOKINGS_FILE = "data/bookings.json"


def show_rooms(rooms: dict[int, dict]) -> None:
    """Вывести список виртуальных комнат."""
    if not rooms:
        print("Список онлайн-комнат пуст.")
        return
    print("\n--- Список онлайн-комнат MeetSync ---")
    for room in rooms.values():
        print(
            f"[{room['id']}] {room['name']} — "
            f"вместимость: {room['capacity']} чел."
        )


def show_bookings(
    bookings: list[dict],
    rooms: dict[int, dict],
) -> None:
    """Вывести список бронирований онлайн-встреч."""
    if not bookings:
        print("Список бронирований пуст.")
        return
    print("\n--- Запланированные онлайн-встречи ---")
    for item in bookings:
        room = rooms.get(item["room_id"])
        room_name = room["name"] if room else f"ID {item['room_id']}"
        print(
            f"Бронь #{item['id']}: {room_name} — "
            f"дата: {item['booking_date']}"
        )


def main() -> None:
    """Запустить главный цикл консольного меню MeetSync."""
    rooms = load_rooms(ROOMS_FILE)
    bookings = load_bookings(BOOKINGS_FILE)

    while True:
        print("\n=== Сервис онлайн-встреч MeetSync ===")
        print("1. Показать онлайн-комнаты")
        print("2. Найти комнату по названию")
        print("3. Проверить вместимость комнаты")
        print("4. Проверить доступность на дату")
        print("5. Забронировать онлайн-комнату")
        print("6. Отменить бронирование")
        print("7. Показать бронирования")
        print("8. Добавить онлайн-комнату")
        print("9. Сортировать и фильтровать комнаты по вместимости")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_rooms(rooms)
        elif choice == "2":
            query = input("Введите подстроку названия: ")
            found = find_room(rooms, query)
            for item in found:
                print(f"[{item['id']}] {item['name']} ({item['capacity']})")
        elif choice == "3":
            room_id = input_int("ID комнаты: ")
            people = input_int("Число участников: ")
            ok = check_room_capacity(rooms, room_id, people)
            print("Помещение подходит" if ok else "Мест недостаточно")
        elif choice == "4":
            room_id = input_int("ID комнаты: ")
            b_date = input_date("Дата (ГГГГ-ММ-ДД): ")
            available = is_room_available(bookings, room_id, b_date)
            print(get_booking_status(available))
        elif choice == "5":
            room_id = input_int("ID комнаты: ")
            b_date = input_date("Дата (ГГГГ-ММ-ДД): ")
            created = create_booking(bookings, room_id, b_date)
            if created:
                save_bookings(BOOKINGS_FILE, bookings)
                print(f"Создано бронирование #{created['id']}")
            else:
                print("Помещение уже занято на выбранную дату")
        elif choice == "6":
            b_id = input_int("ID бронирования: ")
            if cancel_booking(bookings, b_id):
                save_bookings(BOOKINGS_FILE, bookings)
                print("Бронирование отменено.")
            else:
                print("Бронирование не найдено.")
        elif choice == "7":
            show_bookings(bookings, rooms)
        elif choice == "8":
            name = input("Название комнаты: ")
            cap = input_int("Вместимость: ")
            add_room(rooms, name, cap)
            save_rooms(ROOMS_FILE, rooms)
            print("Онлайн-комната добавлена.")
        elif choice == "9":
            min_cap = input_int("Минимальная вместимость: ")
            filtered = list(filter_rooms_by_capacity(rooms, min_cap))
            for item in sort_rooms({r["id"]: r for r in filtered}):
                print(f"[{item['id']}] {item['name']} ({item['capacity']})")
        elif choice == "0":
            save_rooms(ROOMS_FILE, rooms)
            save_bookings(BOOKINGS_FILE, bookings)
            print("До свидания!")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
