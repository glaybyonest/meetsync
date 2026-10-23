# MeetSync — Сервис управления онлайн-встречами

## Назначение
MeetSync — консольное приложение на Python для управления виртуальными
комнатами (онлайн-залами), пользователями и бронированиями онлайн-встреч.
В ПР3 функциональная модель переведена на объектно-ориентированную архитектуру.

## Основные сущности (пакет `models/`)
### `Room` (`models/rooms.py`)
Представляет виртуальную комнату для онлайн-встреч:
- Атрибуты: `id`, `name`, `capacity`, `room_type`, `description`.
- Методы и свойства: `is_suitable_for(people_count)`, `validate_capacity()`,
  `info` (`@property`), `__str__()`.

### `User` (`models/users.py`)
Представляет пользователя (организатора/участника) системы:
- Атрибуты: `id`, `name`, `email`.
- Методы: `from_data(data)` (`@classmethod`), `__str__()`.

### `Booking` (`models/bookings.py`)
Представляет бронирование онлайн-встречи:
- Атрибуты: `id`, `room` (объект `Room`), `booking_date`, `user` (объект
  `User`), `is_cancelled`.
- Методы: `cancel()`, `__str__()`.

## Хранение данных
Данные хранятся в `data/rooms.json`, `data/users.json` и `data/bookings.json`.
Модуль `storage.py` преобразует записи JSON в объекты `Room`, `User`, `Booking`
при загрузке и сохраняет объектные связи через `room_id` и `user_id`.

## Запуск приложения, тестов и проверки кода
```bash
python main.py
pytest -v
flake8 . --extend-exclude=venv
```
