"""
Создание класса
"""
class User:
    """
    Класс для представления пользователя с именем и фамилией.
    """
    def __init__(self, first_name, last_name):
        """
        Инициализирует пользователя с именем и фамилией.
        """
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        """
        Выводит имя пользователя.
        """
        print(self.first_name)

    def print_last_name(self):
        """
        Выводит фамилию пользователя.
        """
        print(self.last_name)

    def print_full_name(self):
        """
        Выводит имя и фамилию пользователя.
        """
        print(f"{self.first_name} {self.last_name}")
