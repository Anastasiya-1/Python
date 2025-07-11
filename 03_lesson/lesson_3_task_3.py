"""
Скрипт для создания и печати сведений о почтовом отправлении.
"""

from address import Address
from mailing import Mailing

to_addr = Address("101000", "Москва", "Арбат", "12", "8")
from_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "1", "30")
mailing = Mailing(to_addr, from_addr, 350, "AB123456789RU")

print(
    f"Отправление {mailing.track} из {mailing.from_address} "
    f"в {mailing.to_address}. Стоимость {mailing.cost} рублей."
)
