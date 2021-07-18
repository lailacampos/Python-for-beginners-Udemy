# Interfaces

# At a high level, an interface acts as a blueprint for designing classes. Like classes, interfaces define methods.
# Unlike classes, these methods are abstract. An abstract method is one that the interface simply defines.
# It doesn't implement the methods.

# Interfaces in Python are abstract classes in which all methods are abstract.

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        # Define formula for calculating area of object
        pass

    @abstractmethod
    def perimeter(self):
        # Define formula for calculating perimeter
        pass

class Rectangle(Shape):

    def __init__(self, lenght, height):
        self.lenght = lenght
        self.height = height

    def area(self):
        area = self.lenght * self.height
        return area

    def perimeter(self):
        perimeter = (2 * self.lenght) + (2 * self.height)
        return perimeter


rectangle = Rectangle(10, 5)
print(rectangle.area())
print(rectangle.perimeter())
