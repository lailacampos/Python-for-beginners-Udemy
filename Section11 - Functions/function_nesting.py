# Function inside another function

def display(name):
    def message():
        return 'Hello '
    return message() + name

print(display('Laila'))
# print(message())  # Cannot access the function because it exists only inside the other function
