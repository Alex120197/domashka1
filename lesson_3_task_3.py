from address import Address
from mailing import Mailing
to_address = Address("12345", "Москва", "Ленина", "10", "20")
from_address = Address("54321", "Самара", "Пушкина", "120", "10")
mailing = Mailing(to_address, from_address, 1500, "123")

print(f"Отправление товара под номером {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.home_number} - {mailing.from_address.apart_number} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.home_number} - {mailing.to_address.apart_number}. Стоимость {mailing.cost} рублей.")
