# Chaining decorators

# A decorator that will return the square value of a function
def decorator_square(function):
    def inner_function(*args, **kwargs):
        value = function(*args, **kwargs)
        print(f'Inside inner function of {decorator_square.__name__}. Result = {value ** value}')
        return value * value
    return inner_function


# A decorator that halves the result of a function
def decorator_half(function):
    def inner_function(*args, **kwargs):
        value = function(*args, **kwargs)
        print(f'Inside inner function of {decorator_half.__name__}. Result = {value/2}')
        return value/2
    return inner_function


@decorator_square
@decorator_half
def num(number):
    print(f'Inside original function. number = {number}')
    return number


# Decorators are applied from bottom to top so changing the order will change the result
@decorator_half
@decorator_square
def num2(number):
    print(f'Inside num2 function. number = {number}')
    return number

# The above is the same thing as:
# num2 = decorator_half(decorator_square(num2(number)))

print(num(10))
print(num2(10))
