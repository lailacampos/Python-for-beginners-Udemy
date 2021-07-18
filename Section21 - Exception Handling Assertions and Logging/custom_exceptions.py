# Creating custom exceptions

# To create a custom exception, use the raise keyword:

# x = 10
# if x > 5:
#     raise Exception(f'x should not exceed 5. The value of x was {x}')

# Alternatively, I can define my own exception class that inherits from the Exception class:

class OverTheLimit(Exception):
    def __init__(self, msg):
        self.msg = msg


def check_value(number):
    if number > 500:
        raise OverTheLimit('Number cannot be bigger than 500')


check_value(1000)
