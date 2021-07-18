# Assert keyword
# https://dbader.org/blog/python-assert-tutorial

# Python’s assert statement is a debugging aid that tests a condition.
# If the condition is true, it does nothing and your program just continues to execute.
# But if the assert condition evaluates to false, it raises an AssertionError exception with an optional error message.

# Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors.
# The goal of using assertions is to let developers find the likely root cause of a bug more quickly.
# An assertion error should never be raised unless there’s a bug in your program.

# assert_statement ::= "assert" expression1 ["," assert message]

# At execution time, the Python interpreter transforms each assert statement into roughly the following:
#
# if __debug__:
#     if not expression1:
#         raise AssertionError(expression2)

x = False

if x:
    print('x is True')
else:
    assert False, ("x is False. This should never happen.")

# DON'T Use Asserts for Data Validation:

# Assertions can be globally disabled with the -O and -OO command line switches, as well as the PYTHONOPTIMIZE
# environment variable in CPython.


