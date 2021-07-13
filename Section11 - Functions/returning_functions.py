# Returning functions from another function

def display():
    def message():
        return 'Hello world'
    return message  # Returns a function

my_function = display()  # Function is being assigned to a variable
print(my_function())
