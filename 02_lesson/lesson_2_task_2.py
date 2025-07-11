"""
Високосный год
"""
def is_year_leap(year):
    """
    Возвращает True, если год високосный, иначе False.
    """
    return year % 4 == 0


YEAR = 2024
RESULT = is_year_leap(YEAR)
print("год", YEAR, ":", RESULT)
