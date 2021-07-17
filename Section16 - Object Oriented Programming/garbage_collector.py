# Garbage collecting in Python

# https://towardsdatascience.com/memory-management-and-garbage-collection-in-python-c1cb51d1612c

# Garbage collection is to release memory when the object is no longer in use.
# This system destroys the unused object and reuses its memory slot for new objects.
# If the memory is not released, the program will use it all and will crash at some point.

# Python is a high-level language and it's not necessary to do the memory management manually.
# Python garbage collection algorithm is very useful to open up space in the memory.

# Garbage collection is implemented in Python in two ways: reference counting and generational.
# When the reference count of an object reaches 0, reference counting garbage collection algorithm cleans up the
# object immediately.

# https://miro.medium.com/max/700/1*Q759CB0_RMWcEfwmOBO85g.png

# Destructors are called when an object gets destroyed. In Python, destructors are not needed as much needed in
# C++ because Python has a garbage collector that handles memory management automatically.

# The __del__() method is a known as a destructor method in Python. It is called when all references to the object
# have been deleted i.e when an object is garbage collected.

class Product:

    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price

    def __repr__(self):
        rep = f'Product(name: {self.name}, description: {self.desc}, price: {self.price})'
        return rep

    # Will be called before it cleans up the memory that is allocated to the instance if that particular object.
    def __del__(self):
        print(f'Deleting {self}')


p1 = Product('Chair', 'Something you can sit on', 40)
print(p1)

p2 = Product('Ball', 'Kick it around and it bounces!', 20)
print(p2)

p1 = None
print(p1)
