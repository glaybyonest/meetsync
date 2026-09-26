import datetime  # Импорт модуля
import math      # Импорт модуля для округления

print("=== Система тарификации MeetSync ===")
print(f"Текущее время в системе: {datetime.datetime.now().strftime('%H:%M:%S')}")
print("Тарифы: 'free' (до 40 мин бесплатно), 'premium' (безлимит)\n")

# Простые типы данных (строки)
user_plan = input("Введите ваш тарифный план (free/premium): ")
duration_str = input("Введите планируемую длительность встречи в минутах: ")

# Преобразование типов (строка -> целое число)
duration_minutes = int(duration_str)
price_per_minute = 3.5  # Цена за каждую минуту сверх лимита

print("\n--- Результат проверки ---")

# Ветвления
if user_plan == "premium":
    print("У вас Premium-аккаунт. Время встречи не ограничено!")
elif user_plan == "free":
    if duration_minutes <= 40:
        print("Встреча укладывается в бесплатный лимит (40 минут). Доплат не требуется.")
    else:
        # НАМЕРЕННАЯ ОШИБКА ЗДЕСЬ:
        # Вместо того чтобы найти разницу (минуты сверх лимита), мы их прибавляем
        overtime = duration_minutes + 40 
        
        # Операции с переменными
        extra_cost = math.ceil(overtime * price_per_minute)
        
        print("Внимание! Превышен бесплатный лимит (40 минут).")
        print("Дополнительное время:", overtime, "мин.")
        print("Стоимость доплаты составит:", extra_cost, "руб.")
else:
    print("Ошибка: Неизвестный тарифный план.")