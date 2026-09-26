import datetime

# Импортируем функции из наших собственных модулей
from billing import calculate_extra_cost
from meeting_manager import schedule_meeting, list_meetings

def main_menu():
    """Главная функция программы, реализующая консольное меню (Сценарий 3)."""
    while True:
        print("\n" + "="*30)
        print("=== Система MeetSync ===")
        print(f"Время: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print("="*30)
        print("1. Рассчитать стоимость встречи (Калькулятор)")
        print("2. Запланировать новую встречу")
        print("3. Показать список встреч")
        print("4. Выйти из программы")
        
        choice = input("\nВыберите действие (введите цифру 1-4): ")
        
        if choice == '1':
            plan = input("Введите тариф (free/premium): ").lower()
            duration_str = input("Введите длительность в минутах: ")
            
            # Добавим базовую защиту от того, что пользователь ввел текст вместо числа
            if duration_str.isdigit():
                cost = calculate_extra_cost(plan, int(duration_str))
                
                if cost == -1.0:
                    print("\n[ОШИБКА] Неизвестный тарифный план!")
                elif cost == 0.0:
                    print("\n[РЕЗУЛЬТАТ] Встреча укладывается в лимиты. Доплат не требуется.")
                else:
                    print(f"\n[РЕЗУЛЬТАТ] Требуется доплата за превышение: {cost} руб.")
            else:
                print("\n[ОШИБКА] Длительность должна быть числом!")
                
        elif choice == '2':
            title = input("Введите тему встречи: ")
            plan = input("Введите тариф (free/premium): ").lower()
            duration_str = input("Введите длительность в минутах: ")
            
            if duration_str.isdigit():
                schedule_meeting(title, int(duration_str), plan)
            else:
                print("\n[ОШИБКА] Длительность должна быть числом!")
                
        elif choice == '3':
            list_meetings()
            
        elif choice == '4':
            print("\nЗавершение работы MeetSync. До свидания!")
            break  # Выход из бесконечного цикла
            
        else:
            print("\n[ОШИБКА] Неверный выбор. Пожалуйста, введите цифру от 1 до 4.")

# Точка входа в программу
if __name__ == "__main__":
    main_menu()