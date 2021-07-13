# Returning multiple values
# In python a function can return multiple values. The values are returned as a tuple and cannot be modified
def calculator(a, b):
    x = a + b
    y = a - b
    w = a * b
    z = a / b
    return x, y, w, z

results = calculator(10, 20)
print(results)
print(type(results))