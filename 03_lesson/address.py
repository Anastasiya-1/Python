"""
Модуль для описания класса Address — почтового адреса.
"""


class Address:
    """
    Класс для представления почтового адреса.
    """

    def __init__(self, index, city, street, house, apartment):
        """
        Инициализирует адрес.

        :param index: Почтовый индекс.
        :param city: Город.
        :param street: Улица.
        :param house: Дом.
        :param apartment: Квартира.
        """
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        """
        Возвращает строковое представление адреса.
        """
        return f"{self.index}, {self.city}, {self.street}, {self.house} - {self.apartment}"
