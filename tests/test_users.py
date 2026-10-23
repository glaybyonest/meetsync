"""Тесты класса User и функций работы с пользователями (ПР3)."""

from models import User
from models.users import add_user, find_user, find_user_by_id


def test_user_creation() -> None:
    """Проверить создание объекта User и строковое представление."""
    user = User(1, "Иван Петров", "ivan@example.com")
    assert user.id == 1
    assert user.name == "Иван Петров"
    assert user.email == "ivan@example.com"
    assert str(user) == "Иван Петров (ivan@example.com)"


def test_user_from_data() -> None:
    """Проверить создание объекта User через @classmethod from_data()."""
    data = {
        "id": 2,
        "name": "Анна Смирнова",
        "email": "anna@example.com",
    }
    user = User.from_data(data)
    assert user.id == 2
    assert user.name == "Анна Смирнова"
    assert user.email == "anna@example.com"


def test_add_and_find_user() -> None:
    """Проверить добавление и поиск объектов User в коллекции."""
    users: list[User] = []
    add_user(users, "Иван Петров", "ivan@example.com")
    add_user(users, "Анна Смирнова", "anna@example.com")
    assert len(users) == 2
    assert find_user_by_id(users, 1) is users[0]
    found = find_user(users, "анна")
    assert len(found) == 1
    assert found[0].email == "anna@example.com"
