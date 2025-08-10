from Smartphone import Smartphone

catalog = []

phones_data = [
    ("iPhone", "15 pro max", "+79271111111"),
    ("iPhone", "11", "+79272222222"),
    ("Xiaomi", "Mi 11", "+79876543210"),
    ("Google", "Pixel 5", "+79765432109"),
    ("OnePlus", "9 Pro", "+79654321098")
]

catalog = [Smartphone(brand, model, phone_number) for (brand, model, phone_number) in phones_data]

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.phone_number}")