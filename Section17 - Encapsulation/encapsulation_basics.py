# Encapsulation basics

class MyClass:

    def __init__(self):
        self.public_attr = 'Public attribute'
        self._private_attr = 'Private attribute by convention. Can still be accessed by the instance obj.'
        self.__private_attr = 'Private attribute. Cannot be accessed by conventional means.'

    def display(self):
        print(self.public_attr)
        print(self._private_attr)
        print(self.__private_attr)

obj = MyClass()
print(obj.public_attr)
print(obj._private_attr)

# print(obj.__private_attr)  # Will result in an error as __ turns an attribute private
print()
obj.display()

print()

# Name mangling
# https://www.geeksforgeeks.org/name-mangling-in-python/
# It's possible to access a private attribute with the following syntax:
# obj. _ClassName __private_field (without spaces)
print(obj._MyClass__private_attr)
