# Глобальный список для хранения встреч в оперативной памяти
meetings_db = []

def schedule_meeting(title: str, duration: int, plan: str):
    """Сценарий 1: Добавляет новую встречу в список."""
    meeting = {
        "title": title,
        "duration": duration,
        "plan": plan
    }
    meetings_db.append(meeting)
    print(f"\n[УСПЕХ] Встреча '{title}' на {duration} мин. успешно запланирована!")

def list_meetings():
    """Сценарий 2: Выводит список всех запланированных встреч."""
    if not meetings_db:
        print("\n[ИНФО] Запланированных встреч пока нет.")
        return
    
    print("\n--- Список ваших встреч ---")
    for idx, meeting in enumerate(meetings_db, start=1):
        print(f"{idx}. {meeting['title']} | Длительность: {meeting['duration']} мин | Тариф: {meeting['plan']}")
    print("---------------------------")