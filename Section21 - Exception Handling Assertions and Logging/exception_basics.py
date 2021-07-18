# Exception basics
# https://realpython.com/python-exceptions/

# A Python program terminates as soon as it encounters an error.
# In Python, an error can be a syntax error or an exception.

# Syntax errors occur when the parser detects an incorrect statement.

# An exception error occurs whenever syntactically correct Python code results in an error.

# If an exception is not handled, three things will happen:
# 1 - The program will terminate abruptly. It will stop wherever the exception was raised and the next line will not be
#     executed.
# 2 - The Python virtual machine will display the unfriendly information to the end user.
# 3 - Improper shutdown of resources. If there are database connections, file streams or network connection opened
#     opened during the application and they are not closed before the line where the exception was raised, then they
#     will remain open.

try:
    a, b = [int(x) for x in input('Enter two numbers: ').split(sep=',')]
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Division by zero not allowed.')
finally:
    print('This will be executed whether an exception is raised or not')
