# Global and local variables

x = 123  # Global variable

def function1():
    y = 321  # Local variable
    print('function1: y =', y)
    print('function1: x =', globals()['x'])  # Will access the global variable instead of the local one

def function2():
    x = 456
    print('function2: x =', x)

print(x)
function1()  # Will print the local variable
function2()  # Local variable takes precedence over global. Will print 456 first then will print the global variable
