class Address:

    def __init__(self, index, city, street, home_number, apart_number):
        self.i = index
        self.c = city
        self.s = street
        self.h = home_number
        self.an = apart_number
    def sayName(self):
     print(self.i)
     print(self.c)
     print(self.s)
     print(self.h)
     print(self.an)