# Decorators

# https://realpython.com/primer-on-python-decorators/

# A decorator is a function that takes another function as an argument and extends the behavior of the latter function
# without explicitly modifying it and then returns another function. It just adds functionality.

# This function takes another function (function) and adds functionality to it, therefore it's a decorator
def decorator_function(function):
    def inner_function():
        print("This happens before the decoration")
        function()
        print("This happens after the decoration")
    return inner_function


def ordinary_function():
    print("Whatever")


ordinary_function = decorator_function(ordinary_function)
ordinary_function()

# This is the equivalent of:
@decorator_function
def ordinary_function2():
    print('Whatever')


ordinary_function2()

########################################################################
# Decorating Functions With Arguments

def decorator_do_twice(function):
    # For the use of * and ** before parameters:
    # https://treyhunner.com/2018/04/keyword-arguments-in-python/
    # *args captures all positional arguments given to the wrapper_do_twice function into a tuple which the args
    # variable points to.
    # **kwargs -> The ** operator will allow the wrapper_do_twice function to accept any number of keyword arguments.
    # The given arguments will be stored in a dictionary called kwargs.
    def wrapper_do_twice(*args, **kwargs):
        function(*args, **kwargs)
        function(*args, **kwargs)
    return wrapper_do_twice

@decorator_do_twice
def some_function():
    print('Something here')

some_function


@decorator_do_twice
def greet(name):
    print(f'Hello {name}')

greet('Laila')

########################################################################
