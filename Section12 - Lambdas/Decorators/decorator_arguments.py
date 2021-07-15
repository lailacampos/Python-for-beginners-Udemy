# Decorators with arguments
# https://realpython.com/primer-on-python-decorators/#decorators-with-arguments
# https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-iii-decorators-with-arguments

# Python always passes the decorated function as a single argument to the decorator function, so there is really no
# place where decorator arguments can be added in the original function.

# For that reason, decorators with arguments are built on top of standard decorators.
# A decorator with arguments is defined as a function that returns a standard decorator.

import functools


# Without arguments:

# def my_decorator(f):
#     def wrapped(*args, **kwargs):
#         print('Before function')
#         response = f(*args, **kwargs)
#         print('After function')
#         return response
#
#     print('Decorating', f)
#     return wrapped
#
#
# @my_decorator
# def my_function(a, b):
#     print('Inside function')
#     return a + b

# With arguments:

# Decorators with arguments are built on top of standard decorators
# It returns a standard decorator (inner_decorator)
def my_decorator(arg):
    def inner_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print('Before function')
            value = function(*args, **kwargs)
            print('After function')
            return value

        print(f'Decorating {function} with argument {arg}')
        return wrapper

    return inner_decorator


@my_decorator('arg')
def my_function(a, b):
    print('Inside function')
    return a + b


# my_function = my_decorator('arg')(my_function)
my_function(3, 4)
