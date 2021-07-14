# Decorators with arguments
# https://realpython.com/primer-on-python-decorators/#decorators-with-arguments

# Writing a decorator to repeat a function a number of times

def repeat(num_times):
    def decorator_function(function):

