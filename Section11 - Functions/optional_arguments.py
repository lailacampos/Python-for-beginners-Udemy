# Optional arguments
# A function can have optional arguments
# Arguments can have default values

# Python Arbitrary Arguments:
# Sometimes, we do not know in advance the number of arguments that will be passed into a function. Python
# allows us to handle this kind of situation through function calls with an arbitrary number of arguments. In the
# function definition, we use an asterisk (*) before the parameter name to denote this kind of argument.

# https://www.programiz.com/python-programming/function-argument

# Default values
def greet(name, msg='how are you?'):
    print('Hello {}, {}'.format(name, msg))


greet('Laila')  # If no value is passed, uses default value
greet(name='Laila', msg='good morning')
greet('Laila', msg='good afternoon')


# greet(msg='are you okay?', 'Laila')  # Positional argument must come before keyword argument

################################################################
# Python Arbitrary Arguments
# Use an asterisk (*) before the parameter name to denote we do not know in advance
# the number of arguments that will be passed into a function

def greet2(*names):
    for name in names:
        print('Hello ', name)


greet2('Laila', 'Ricardo', 'João')


################################################################

# Python Arbitrary Keyword Arguments
def greet3(**kwargs):
    for key, value in kwargs.items():
        print('{} = {}'.format(key, value))


greet3(name='Laila', msg=', how are you?')


################################################################
# Passing optional parameters to other functions

def function(*args, **kwargs):
    modified_args = args + (40,)
    kwargs['id'] = 123
    function2(modified_args, kwargs)


def function2(*arbitrary_parameter, **keyword_arbitrary_parameter):
    print(arbitrary_parameter)
    print(keyword_arbitrary_parameter)

function(10, 20, 30, name='Laila', age=30)
