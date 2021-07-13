# Map() function

# map() is a built-in function that allows you to process and transform all the items in an iterable without using an
# explicit for loop, a technique commonly known as mapping.

# map() loops over the items of an input iterable (or iterables) and returns an iterator that results from applying a
# transformation function to every item in the original input iterable.

# map(function, iterable[, iterable1, iterable2,..., iterableN]) The first argument to map() is a function object,
# which means that you need to pass a function without calling it. That is, without using a pair of parentheses.

# #################################################################
# Examples:
# Taking a list of numeric values and transforming it into a list containing the square value of every number in the
# original list

numbers = [1, 2, 3, 4, 5]
squared = []

# With a for loop:
for i in numbers:
    squared.append(i ** 2)

print(squared)


# Using the map() function with a user-defined function
# map(function, iterable[, iterable1, iterable2,..., iterableN])
def square(number):
    return number ** 2


# map() returns a map object, which is an iterator that yields items on demand
squared = map(square, numbers)
print(list(squared))

# Using the map() function with a lambda function
squared = map(lambda x: x**2, numbers)
print(list(squared))
