"""
Модуль для описания класса Mailing — почтового отправления.
"""

from address import Address

class Mailing:
    """
    Класс для представления почтового отправления.
    """

    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str):
        """
        Инициализирует почтовое отправление.
        :param to_address: Адрес получателя (Address).
        :param from_address: Адрес отправителя (Address).
        :param cost: Стоимость отправления (float/int).
        :param track: Трек-номер (str).
        """
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
