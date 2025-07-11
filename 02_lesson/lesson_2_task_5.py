"""
Месяц — сезон
"""

def month_to_season(month):
    """
    Возвращает название сезона по номеру месяца.
    1 — январь, 12 — декабрь.
    """
    if month in (12, 1, 2):
        return "Зима"
    if month in (3, 4, 5):
        return "Весна"
    if month in (6, 7, 8):
        return "Лето"
    if month in (9, 10, 11):
        return "Осень"
    return "Некорректный номер месяца"


print(month_to_season(2))
print(month_to_season(5))
print(month_to_season(7))
print(month_to_season(10))
print(month_to_season(13))
