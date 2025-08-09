class User:

    def __init__(self, first_name, last_name):
     print()
     self.first_name=first_name
     self.last_name=last_name

        
    def sayName(self):
       
       print(self.first_name)
       print(self.last_name)
       print(self.first_name, self.last_name)

name = User("Саша", "Власов")
name.sayName()
    