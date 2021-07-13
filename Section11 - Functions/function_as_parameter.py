# Functions as parameters to other functions

def display(function):
    return 'Hello ' + function  # Returns 'Hello' plus whatever the other function returns

def display_name(name):
    return name

print(display(display_name('Laila')))
