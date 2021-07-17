# The __init__() Function

# All classes have a function called __init__(), which is always executed when the class is being initiated. Use the
# __init__() function to assign values to object properties, or other operations that are necessary to do when the
# object is being created.

# __init__() sets the initial state of the object by assigning the values of the object’s properties.
# That is, .__init__() initializes each new instance of the class.

# The self parameter is a reference to the current instance of the class, and is used to access variables that
# belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the
# first parameter of any function in the class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('Laila', 30)

print(person.name, person.age)