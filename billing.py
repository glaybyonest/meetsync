import math

def calculate_extra_cost(user_plan: str, duration_minutes: int) -> float:
    """
    Функция рассчитывает стоимость превышения лимита встречи.
    Возвращает сумму доплаты или 0.0, если доплата не требуется.
    Возвращает -1.0 в случае ошибки тарифа.
    """
    price_per_minute = 3.5  # Цена за каждую минуту сверх лимита
    
    if user_plan == "premium":
        return 0.0
    elif user_plan == "free":
        if duration_minutes <= 40:
            return 0.0
        else:
            # Правильная логика: вычитаем бесплатные 40 минут
            overtime = duration_minutes - 40
            return math.ceil(overtime * price_per_minute)
    else:
        return -1.0  # Код ошибки для неизвестного тарифа