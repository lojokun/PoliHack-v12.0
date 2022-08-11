class Person():
    def __init__(self, name, surname, gender, age, pers_ID_nr):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.pers_ID_nr = pers_ID_nr
    def retirement(self):
        if self.gender == "female":
            if self.age >= 60:
                print("This person has reached the retirement age")
            else:
                print("This person has not reached the retirement age")
        else:
            if self.age >= 65:
                print("This person has reached the retirement age")
            else:
                print("This person has not reached the retirement age")
person1=Person("Alex", "Vulcan", "male", 70, 180320)
person1.retirement()
        
