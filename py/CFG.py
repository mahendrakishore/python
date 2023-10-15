
class Person:

    animal = 'dog'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"{self.name} and {self.age}")

person = Person("John", 30)
print(person.name)
print(person.age)
person.show()

