# Inheritance basics

# Inheritance is the mechanism of basing an object or class upon another object (prototype-based inheritance) or
# class (class-based inheritance), retaining similar implementation.

# https://realpython.com/inheritance-composition-python/#whats-inheritance


# Classes from which other classes are derived are called base classes or super classes.
class MySuperClass:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f'MySuperClass ({self.name}, {self.number})'

    def super_display(self):
        print(self.name)
        print(self.number)

    @staticmethod
    def random_method():
        print('Doing something...')


# Classes that inherit from another are called derived classes, subclasses, or subtypes.
# A derived class is said to derive, inherit, or extend a base class.
class MySubClass(MySuperClass):

    # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, name, number, description):
        
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
        # MySuperClass.__init__(self, name, age)
        
        # Alternatively, use the super() method.
        super().__init__(name, number)
        self.description = description

    def __repr__(self):
        return f'MySubClass ({self.name}, {self.number}, {self.description})'

    def sub_display(self):
        print(self.name)
        print(self.number)
        print(self.description)

    # Overriding the parent's method
    @staticmethod
    def random_method():
        print('Doing something else...')


super_object = MySuperClass('Super Object', 10)
sub_object = MySubClass('Sub object', 20, 'Random object')

super_object.super_display()
super_object.random_method()

print()
sub_object.sub_display()
sub_object.random_method()
