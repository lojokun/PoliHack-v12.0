class Dog():
    def __init__(self, name, is_hungry):
        self.name = name
        self.is_hungry = is_hungry
    def eat(self):
        if self.is_hungry == True:
            is_hungry = False
    def bark(self):
        print("Woof, woof!")
dog1 = Dog("Buddy", True)
dog1.is_hungry
dog1.eat()
dog1.is_hungry
dog1.name
dog1.bark()
