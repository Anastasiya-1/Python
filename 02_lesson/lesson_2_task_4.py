"""
Задачка с собеседования
"""
def fizz_buzz(n):
    """
    Выводит числа от 1 до n включительно.
    Вместо чисел, кратных 3, выводит 'Fizz',
    вместо кратных 5 — 'Buzz',
    вместо кратных 3 и 5 одновременно — 'FizzBuzz'.
    :param n: Верхний предел диапазона (включительно).
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(17)
