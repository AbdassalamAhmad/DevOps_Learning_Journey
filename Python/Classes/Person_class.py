class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print (f"Hello I am {self.name}")

samir = Person("samir")

samir.talk()

