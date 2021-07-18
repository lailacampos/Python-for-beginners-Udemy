# Polymorphism with Functions and Objects
# https://www.edureka.co/blog/polymorphism-in-python/

# In programming, Polymorphism refers to the use of a single type entity (method, operator or object) to represent
# different types in different scenarios.

# Also known as Duck Typing
# With functions and objects:
class Tomato:

    def type(self):
        print('Vegetable')

    def color(self):
        print('Red')


class Orange:

    def type(self):
        print('Fruit')

    def color(self):
        print('Orange')


def display(obj):
    obj.type()
    obj.color()


tomato = Tomato()
orange = Orange()
print()
# display() is a function that can take any object, allowing for polymorphism.
# Display behaves in a different way depending of the parameter.
display(tomato)
display(orange)
print()
###################################################################################
# Example 2:


class Duck:

    def talk(self):
        print('Quack quack')


class Human:

    def talk(self):
        print('Hello')


def call_talk(obj):
    obj.talk()


duck = Duck()
human = Human()

# The same function can do multiple things depending on what parameter is passed at run time
call_talk(duck)
call_talk(human)
