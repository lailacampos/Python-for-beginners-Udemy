# Reduce() function

#  reduce() is a function that implements a mathematical technique called folding or reduction.
#  reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.

# Python’s reduce() operates on any iterable—not just lists—and performs the following steps:
#
# 1 - Apply a function (or callable) to the first two items in an iterable and generate a partial result.
# 2 - Use that partial result, together with the third item in the iterable, to generate another partial result.
# 3 - Repeat the process until the iterable is exhausted and then return a single cumulative value.

# reduce() works by applying a two-argument function to the items of iterable in a loop from left to right,
# ultimately reducing iterable to a single cumulative value.

# functools.reduce(function, iterable[, initializer])
# The first argument to Python’s reduce() is a two-argument function conveniently called function.
# This function will be applied to the items in an iterable to cumulatively compute a final value.
#
# The second required argument, iterable, will accept any Python iterable, as its name suggests.
# This includes lists, tuples, range objects, generators, iterators, sets, dictionary keys and values,
# and any other Python objects that you can iterate over.

# First import the function
from functools import reduce

# Example 1 -> Sum of items in a iterable
# Computes the sum of two numbers and prints the equivalent math operation to the screen
def my_add(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result


numbers = [0, 1, 2, 3]

print(reduce(my_add, numbers))

##########################################################
# The third parameter -> Initializer
# functools.reduce(function, iterable[, initializer])

# If a value is supplied to initializer, then reduce() will feed it to the first call of function as its first argument.
# This means that the first call to function will use the value of initializer and the first item of iterable to
# perform its first partial computation.
# After this, reduce() continues working with the subsequent items of iterable.

print(reduce(my_add, numbers, 100))

# Using reduce() with a lambda function:
print(reduce(lambda a, b: a + b, numbers))

##########################################################
# Example 2 -> multiplication of items in a iterable

numbers2 = [1, 2, 3, 4]

# Using a user-defined function
def my_product(a, b):
    result = a * b
    print(f'{a} * {b} = {result}')
    return result


print(reduce(my_product, numbers2))

# Using lambda functions
print(reduce(lambda a, b: a*b, numbers2))