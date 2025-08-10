from address import Address
from mailing import Mailing
to_address = Address
from_address = Address
to_address = 111111, "г. Самара", "ул. Ленина", 120, 7
from_address = 222222, "г. Москва", "ул. Пушкина", 25, 17
sending = Mailing (to_address, from_address, 1500, 12345)
print(
    "Отправление товара под номером",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)