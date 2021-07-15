# Decorator that repeats a function n times (with parameters)
# https://realpython.com/primer-on-python-decorators/#decorators-with-arguments

from functools import wraps

# Outer function that will take the parameter
def repeat(num_times=1):

    # Actual decorator that takes the function as parameter
    def decorator_repeat(function):
        @wraps(function)

        # Wrapper function which will take the place of the original function
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = function(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('World')
