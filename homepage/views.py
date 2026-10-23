"""Представления (view-функции) приложения homepage (ПР5)."""
from django.http import HttpResponse


def page(title: str, content: str) -> str:
    """Собрать единый HTML-каркас страницы с подключением Bootstrap 5.3."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body>
    <nav class="nav border-bottom mb-4 p-2">
        <a class="nav-link" href="/">Главная</a>
        <a class="nav-link" href="/rooms/">Онлайн-комнаты</a>
        <a class="nav-link" href="/bookings/">Онлайн-встречи</a>
    </nav>
    <main class="container">{content}</main>
</body>
</html>"""


def index(request):
    """Главная страница веб-интерфейса MeetSync."""
    content = """
    <h1 class="display-4">MeetSync</h1>
    <p class="lead">
        Сервис управления онлайн-встречами и виртуальными комнатами.
    </p>
    <p>Основные разделы:</p>
    <a href="/rooms/" class="btn btn-primary me-2">Онлайн-комнаты</a>
    <a href="/bookings/" class="btn btn-secondary">Онлайн-встречи</a>
    """
    return HttpResponse(page("MeetSync", content))


def page_not_found(request, exception):
    """Пользовательский обработчик ошибки 404."""
    content = """
    <h1 class="text-danger">404 – страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную страницу MeetSync.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 – страница не найдена", content),
        status=404,
    )
