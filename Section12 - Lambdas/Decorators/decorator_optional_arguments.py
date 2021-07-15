# Decorators with optional arguments
# https://realpython.com/primer-on-python-decorators/#both-please-but-never-mind-the-bread

# About *args and **kwargs: https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

# Reminder: When a decorator uses arguments, an outer function needs to be added (one more layer)

# Since the function to decorate is only passed in directly if the decorator is called without arguments,
# the function must be an optional argument
# This means that the decorator arguments must all be specified by keyword

# Boilerplate:

# 1 - If name has been called without arguments, the decorated function will be passed in as _function.
# If it has been called with arguments, then _func will be None, and some of the keyword arguments may have been
# changed from their default values. The * in the argument list means that the remaining arguments can’t be called
# as positional arguments.
# def name(_function=None, *, keyword1=value1, keyword2=value2, ...): # 1
#     def decorator_name(function):
#         #... Create and return wrapper function
#
#     # In this case, the decorator was called with arguments. Return a decorator function that can read and return
#     # a function.
#     if _function is None:
#         return decorator_name  # 2
#     else:
#
#         #In this case, the decorator was called without arguments. Apply the decorator to the function immediately.
#         return decorator_name(_function)  # 3

from functools import wraps


# If repeat is called WITHOUT arguments, the original function will be passed in as _function (the keywords arguments
# have default values in case they are not specified)
# If it's called WITH arguments, that means the keywords will be specified while _function will not, therefore _function
# will default to None.
def repeat(_function=None, *, num_times=1):
    def decorator_repeat(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = function(*args, **kwargs)
            return value

        return wrapper

    # If repeat is called WITH arguments, then return a decorator function that can read and return a function, but do
    # not call it immediately.
    if _function is None:
        return decorator_repeat
    else:

        # If repeat is called WITHOUT arguments, then apply the decorator to the original function immediately.
        return decorator_repeat(_function)


@repeat
def say_hello(name):
    print(f'Hello {name}')


@repeat(num_times=3)
def say_goodbye(name):
    print(f'Good bye {name}')


say_hello('Laila')
say_goodbye('Laila')
