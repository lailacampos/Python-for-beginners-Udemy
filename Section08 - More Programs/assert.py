# The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code
# returns True, if not, the program will raise an AssertionError

number = int(input("Enter a number greater than 10: "))

#If the condition evaluates to true, the error message will not be displayed.
assert number > 10, 'This number is not greater than 10'
print('You entered ', number)
