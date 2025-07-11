"""
Площадь квадрата
"""
import math
def square(length):
    """
    Вычисляет площадь квадрата.
    """
    area = length * length
    return math.ceil(area)

SIDE_LENGTH = 5
result = square(SIDE_LENGTH)
print("Площадь квадрата:", result)
