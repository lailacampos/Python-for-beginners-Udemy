# Pythonic way of creating getters and setters and the Property decorator
# https://www.python-course.eu/python3_properties.php
# https://www.freecodecamp.org/news/python-property-decorator/

class Programmer:
    def __init__(self, name, salary, techs):
        self._name = name
        self._salary = salary
        self._techs = techs

    # Getter method without using property decorator:
    # def get_name(self):
    #     return self._name

    # Setter method without using property decorator:
    # def set_name(self, name):
    #     self._name = name

    # Getter using the property decorator:
    @property
    def name(self):
        return self._name

    # Setter using the property decorator:
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Getter and setter for salary:
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    # Getter and setter for techs
    @property
    def techs(self):
        return self._techs

    @techs.setter
    def techs(self, new_techs):
        self._techs = new_techs


p1 = Programmer('Laila', 5000, ['Python', 'Java', 'C#'])
print(p1.name)
print(p1.salary)
print(p1.techs)
