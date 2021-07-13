# Measure the time a function takes to execute
# https://realpython.com/primer-on-python-decorators/#timing-functions

import functools
import time

# Decorator boilerplate:
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator


def timer(function):
    # Print the runtime of the decorated function
    @functools.wraps(function)
    def wrapper_timer(*args, **kwargs):
        # perf_counter() returns the value (in fractional seconds) of a performance counter, i.e. a clock with the
        # highest available resolution to measure a short duration

        # Stores the time just before the function starts running
        start_time = time.perf_counter()
        value = function(*args, **kwargs)

        # Stores the time just after the function stops running
        end_time = time.perf_counter()

        # The time the function takes is then the difference between the end time and teh start time
        run_time = end_time - start_time

        # About !r: https://realpython.com/operator-function-overloading/#representing-your-objects-using-repr
        print(f'Finished {function.__name__!r} in {run_time:.4f} secs')

        # Returns the function passed as argument
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for i in range(num_times):

        # sum() function calculates the total of all numerical values in an iterable
        sum([i**2 for i in range(10)])


waste_some_time(10)
waste_some_time(1000)
