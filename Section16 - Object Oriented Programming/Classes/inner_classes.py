# Inner classes in Python

# https://www.geeksforgeeks.org/inner-class-in-python/
# https://www.geeksforgeeks.org/inheritance-in-python-inner-class/

class OuterClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = f'OuterClass(name: {self.name}, age: {self.age})'
        return rep

    def outer_method(self):
        print(f'Outer method of {self}')

    class InnerClass:

        def __init__(self, description):
            self.description = description

        def __repr__(self):
            rep = f'InnerClass(description: {self.description})'
            return rep

        def inner_method(self):
            print(f'Inner method of {self}')


outer = OuterClass('Laila', 30)
outer.outer_method()

# Creating an instance of the inner class:
inner = outer.InnerClass('Cool person')
inner.inner_method()
