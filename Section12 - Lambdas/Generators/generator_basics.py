# Generator basics

# https://realpython.com/introduction-to-python-generators/
# Generator functions are a special kind of function that return a lazy iterator.
# When a generator function is called or generator expression is used, a special iterator called a generator is
# returned.
# This generator can be assigned to a variable in order to be used.

# Lazy iterators are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store
# their contents in memory.
# About lazy iterators and generators: https://pycon2019.trey.io/iterator-protocol.html#the-iterator-protocol

# Generators are a great way to optimize memory
# Use case: A common use case of generators is to work with data streams or large files, like CSV files.
# Generators use the yield statement instead of return

# Yield:
# Using yield will result in a generator object.
# Using return will result in the first line of the file only
# https://realpython.com/introduction-to-python-generators/#understanding-the-python-yield-statement

def infinite_sequence():
    num = 0
    while True:

        # yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the
        # function afterwards.
        # Instead, the state of the function is remembered. That way, when next() is called on a generator object
        # (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented,
        # and then yielded again.
        yield num
        num += 1


# for i in infinite_sequence():
#     print(i, end=' ')


# Instead of using a for loop, it's possible to also call next() on the generator object directly to manually iterate
# over by repeatedly calling next()
generator = infinite_sequence()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

