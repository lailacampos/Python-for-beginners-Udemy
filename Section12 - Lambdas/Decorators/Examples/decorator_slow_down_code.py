# Slow down a function before calling it

import functools
import time


def slow_down(function):
    # Sleep 1 second before calling the function
    @functools.wraps(function)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return function(*args, **kwargs)

    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print('The countdown reached its end')
    else:
        print(from_number)
        countdown(from_number - 1)


countdown(5)
