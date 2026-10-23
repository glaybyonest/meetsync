# MeetSync – сервис управления онлайн-встречами

Сервис управления онлайн-встречами и виртуальными комнатами на Python и Django.

## 1. Назначение проекта
MeetSync – учебное приложение для управления виртуальными залами (Zoom, Meet,
Teams) и расписанием онлайн-встреч.

## 2. Используемые технологии (ПР6)
- Python 3;
- Django 5.2;
- Django Template Language (DTL);
- HTML5, CSS3, JavaScript, Bootstrap 5.3;
- JSON для хранения данных (`data/rooms.json`, `users.json`, `bookings.json`);
- Git, pytest, flake8.

## 3. Шаблонная архитектура и статика (ПР6)
- Базовый шаблон: `templates/base.html` (`{% block title %}`, `{% block content %}`);
- Включаемые шаблоны (`{% include %}`):
  - `templates/includes/navigation.html`
  - `rooms/templates/rooms/includes/room_card.html`
  - `bookings/templates/bookings/includes/booking_status.html`
- Фильтры шаблонов: `{{ rooms|length }}`, `{{ room.name|default:"Без названия" }}`;
- Именованные маршруты и пространства имён: `homepage:index`, `rooms:list`,
  `rooms:detail`, `bookings:bookings`, `bookings:detail`;
- Статические файлы (`homepage/static/homepage/`): `css/style.css`,
  `js/main.js`, `img/logo.png`;
- Функция `page()` из ПР5 полностью удалена; все представления используют
  `render(request, ..., context)`.
- Данные пока хранятся в JSON; Django ORM и формы ещё не используются.
