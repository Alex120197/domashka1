class Smartphone:

    def __init__(self, brand, model, number):
        print()
        self.b = brand
        self.m = model
        self.n = number
    def sayName(self):
       
       print(self.b)
       print(self.m)
       print(self.n)

name = Smartphone("iPhone", "15 pro max", "+79275555555")
name.sayName()
    