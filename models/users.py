"""Класс User и функции работы с пользователями системы MeetSync (ПР3)."""

from typing import List, Optional


class User:
    """Пользователь (организатор или участник онлайн-встреч) в MeetSync."""

    def __init__(
        self,
        user_id: int,
        name: str,
        email: str,
    ) -> None:
        """Создать объект пользователя системы."""
        clean_name = str(name).strip()
        clean_email = str(email).strip()
        if not clean_name:
            raise ValueError("Имя пользователя не может быть пустым")
        if "@" not in clean_email:
            raise ValueError("Некорректный адрес электронной почты")
        self.id: int = int(user_id)
        self.name: str = clean_name
        self.email: str = clean_email

    @classmethod
    def from_data(cls, data: dict) -> "User":
        """Создать объект User из словаря данных JSON."""
        return cls(
            user_id=int(data["id"]),
            name=str(data["name"]),
            email=str(data["email"]),
        )

    def __str__(self) -> str:
        """Вернуть строковое представление пользователя."""
        return f"{self.name} ({self.email})"


def add_user(
    users: List[User],
    name: str,
    email: str,
) -> None:
    """Создать объект User и добавить его в коллекцию users."""
    next_id = max((user.id for user in users), default=0) + 1
    new_user = User(user_id=next_id, name=name, email=email)
    users.append(new_user)


def find_user_by_id(
    users: List[User],
    user_id: int,
) -> Optional[User]:
    """Найти пользователя по его идентификатору."""
    for user in users:
        if user.id == user_id:
            return user
    return None


def find_user(
    users: List[User],
    query: str,
) -> List[User]:
    """Найти пользователей по имени или адресу электронной почты."""
    needle = query.strip().lower()
    return [
        user
        for user in users
        if needle in user.name.lower() or needle in user.email.lower()
    ]


def show_users(users: List[User]) -> None:
    """Вывести информацию о пользователях в консоль."""
    if not users:
        print("Пользователи не найдены.")
        return
    for user in users:
        print(f"[{user.id}] {user}")
