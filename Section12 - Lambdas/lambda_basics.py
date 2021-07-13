# Lambda functions in Python

# How to define a lambda:
# lambda argument_list : expression

fun = lambda x: x ** x
print(fun(3))

# Alternatively:
# It's possible to apply the lambda function to an argument by surrounding the function and its argument with
# parentheses
print((lambda x: x ** x)(3))


# Equivalent:
def power(x):
    return x ** x


##############################################
# Multiple parameter in a lambda function

print((lambda x, y: x + y)(2, 3))
