class Person:
    def __init__(self, name, description, age):
        self.name = name
        self.description = description
        self.age = age

    def walk(self):
        print('Walking...')


person = Person('Laila', 'A super cool person. Also likes cats.', 30)
print(person.name)
print(person.description)
print(person.age)
person.walk()
