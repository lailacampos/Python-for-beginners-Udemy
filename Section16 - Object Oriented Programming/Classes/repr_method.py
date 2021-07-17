# The __repr__ method
# https://www.educative.io/edpresso/what-is-the-repr-method-in-python

# __repr__ is used to compute the “official” string representation of an object and is typically used for debugging.

class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        rep = f'MyClass({self.a}, {self.b})'
        return rep


obj = MyClass('a', 'b')
print(obj)  # Without the __repr__ method: <__main__.MyClass object at memory_location
