# The yield statement

# The yield primary job is to control the flow of a generator function in a way that’s similar to return statements.

# When a generator function is called or generator expression is used, a special iterator called a generator is
# returned.
# This generator can be assigned to a variable in order to be used.

# When the Python yield statement is hit, the program suspends function execution and returns the yielded value to
# the caller.
# In contrast, return stops function execution completely.
# When a function is suspended, the state of that function is saved.
# This includes any variable bindings local to the generator, the instruction pointer, the internal stack,
# and any exception handling.

def multi_yield():
    yield_str = 'This is the first string'
    yield yield_str
    yield_str = 'This is the second string'
    yield yield_str


multi_obj = multi_yield()
print(next(multi_obj))  # This is the first string

print(next(multi_obj))  # This is the second string

print(next(multi_obj))  # Stop iteration error
