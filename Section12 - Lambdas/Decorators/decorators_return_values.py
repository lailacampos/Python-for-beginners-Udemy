# Returning Values From Decorated Functions

import functools

# Reminder about decorators:
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # original_function(*args, **kwargs)

        # If the this function doesn't return the original_function, the return type when calling the decorated function
        # will be None
        return original_function(*args, **kwargs)

    return wrapper_function


def display():
    print("Display function executed")


decorated_display = decorator_function(display)
decorated_display()


########################################################################


@decorator_function
def greet(name):
    return f'Hello {name}'


hi_laila = greet('Laila')
# Because the wrapper function doesn't explicitly returns a value, the call return ends up returning none
# To fix this, the wrapper function needs to return the value of the decorated function
print(hi_laila)

