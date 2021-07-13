# functools.wraps decorator

# This decorator copies the lost metadata from the undecorated function to the decorated closure.
# It is advisable and good practice to always use functools.wraps when defining decorators.
# It will save a lot of headache in debugging.

# if the functools.wraps decorator is not applied, the decorated function's name, docstring and parameter will be
# hidden by the wrapper closure

# More in https://realpython.com/primer-on-python-decorators/#who-are-you-really
import functools


def decorator_function(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

@decorator_function
def greet(name):
    print('Hello ')


