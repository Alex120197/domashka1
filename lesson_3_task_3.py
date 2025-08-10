class Address:
    
    def __init__(self, index, city, street, home_number, apart_number):
        self.i = index
        self.c = city
        self.s = street
        self.h = home_number
        self.an = apart_number
    
        from address import Address

class Mailing:
    to_address = "Address"
    from_address = "Address"
    cost = "1500"
    track = "12345"

    def __init__(self, to_address, from_address, cost, track):
        self.t = to_address
        self.f = from_address
        self.c = cost
        self.t = track

    def to_address(self):
        print(self.to_address)

    def from_address(self):
        print(self.from_address)


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