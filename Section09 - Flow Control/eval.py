# eval.py

# The eval() function interprets an expression as a python code.
# Python’s eval() allows you to evaluate arbitrary Python expressions from a string-based or compiled-code-based input.
list1 = input('Enter a list: ')
print(list1)  # Prints a string
print(type(list1))  # String type

print()

# eval():
# 1 - Parses expression
# 2 - Compiles it to bytecode
# 3 - Evaluates it as a Python expression
# 4 - Returns the result of the evaluation
list1 = eval(list1)
print(list1)
print(type(list1))

