"""
Модуль с классом Smartphone, представляющим смартфон с маркой,
моделью и абонентским номером.
"""

class Smartphone:
    """
    Класс для представления смартфона с маркой, моделью и абонентским номером.
    """

    def __init__(self, brand, model, phone_number):
        """
        Инициализирует смартфон.

        :param brand: Марка телефона.
        :param model: Модель телефона.
        :param phone_number: Абонентский номер телефона.
        """
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
