# Filter() function
# More info: https://realpython.com/python-filter-function/

#  filter() is a built-in function that allows you to process an iterable and extract those items that
#  satisfy a given condition

# Filtering applies a predicate, or Boolean-valued, function to an iterable and generates a new
# iterable containing the items that satisfy the Boolean condition


num = [-3, -2, -1, 0, 1, 2, 3]


# Doing it with a user-defined function:
def extract_positive(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:  # Filtering condition
            positive_numbers.append(number)
    return positive_numbers


# Using the filter() function

# filter(function, iterable)
# The first argument, function, must be a single-argument function.
# A function that returns either True or False according to a specific condition

# The second argument, iterable, can hold any Python iterable, such as a list, tuple, or set.
# It can also hold generator and iterator objects. An important point regarding filter() is
# that it accepts only one iterable.

# filter() with lambda function

positive_numbers = filter(lambda x: x > 0, num)
# filter() returns a filter object, which is an iterator that yields items on demand.
print(list(positive_numbers))


# filter() with user-defined function
def is_positive(n):
    return n > 0


print(list(filter(is_positive, num)))
