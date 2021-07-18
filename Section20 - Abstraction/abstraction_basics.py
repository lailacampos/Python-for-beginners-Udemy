# Abstraction basics
# https://www.geeksforgeeks.org/abstract-classes-in-python/

# An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods
# that must be created within any child classes built from the abstract class.

# A class which contains one or more abstract methods is called an abstract class.

# An abstract method is a method that has a declaration but does not have an implementation.

# You cannot create an object of a abstract class

# By default, Python does not provide abstract classes.
# Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
# ABC works by decorating methods of the base class as abstract and then registering concrete classes as
# implementations of the abstract base.

from abc import ABC, abstractmethod


class Animal(ABC):

    # A method becomes abstract when decorated with the keyword @abstractmethod.
    @abstractmethod
    def talk(self):
        pass

    # Non-abstract method
    def be_born(self):
        print('Life starts!')


class Human(Animal):

    def talk(self):
        print('Hello')


class Dog(Animal):

    def talk(self):
        print('Bark bark')


# animal = Animal()  # Animal cannot be instantiated because Animal is an abstract class
person = Human()
person.talk()

dog = Dog()
dog.talk()
