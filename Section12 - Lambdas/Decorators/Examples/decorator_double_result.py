# Decorator that doubles the result of a function
from functools import wraps

def decorator(function):
    @wraps(function)
    def inner_function(*args, **kwargs):
        value = function(*args, **kwargs)
        return value * 2
    return inner_function

@decorator
def original_function(a, b):
    return a + b


decorated_function = original_function(2, 2)
print(decorated_function)
