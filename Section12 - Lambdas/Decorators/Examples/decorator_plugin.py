# Decorators don't have to wrap the function they're decorating.
# They can also simply register that a function exists and return it unwrapped.

import random

# This constant is a empty dictionary
# This is the same as: PLUGIN = {}
PLUGINS = dict()


# Decorator function
def register(function):
    # Register a function as a plugin
    # Function name is the Key
    # The function itself is the value
    PLUGINS[function.__name__] = function

    # Returns the function without calling it
    return function


@register
def say_hello(name):
    return f'Hello {name}'


@register
def say_bye(name):
    return f'Good bye {name}'


@register
def say_good_morning(name):
    return f'Good morning {name}'


@register
def say_good_afternoon(name):
    return f'Good afternoon {name}'


def randomly_greet(name):
    # greeter -> Key (function name)
    # greeter_function -> Value (the function itself)

    # The choice() method returns a randomly selected element from the specified sequence
    # list() function -> https://www.programiz.com/python-programming/methods/built-in/list
    greeter, greeter_function = random.choice(list())



