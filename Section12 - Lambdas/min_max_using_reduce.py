# Finding the min and max values of a list using reduce()
# https://realpython.com/python-reduce-function/

from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7]


# Minimum
def find_min_value(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value


def find_max_value(lst):
    # Unpacking and packing -> https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480
    max_value, *rest = lst  # max_value = lst[0], rest = lst[1:]
    for i in rest:
        if i > max_value:
            max_value = i
    return max_value

print(find_min_value(lst))
print(find_max_value(lst))

##########################################################
# Using reduce() with user-defined functions
def my_min_function(a, b):
    return a if a < b else b


def my_max_function(a, b):
    return a if a > b else b


# reduce() iterates over the items of numbers, compares them in cumulative pairs, and finally returns the minimum
# or maximum value.
print(reduce(my_min_function, lst))
print(reduce(my_max_function, lst))
