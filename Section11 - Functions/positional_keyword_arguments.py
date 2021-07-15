# Positional and keyword arguments
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

# To accept keyword-only arguments, we can put named arguments after a * usage when defining our function

def get_multiple(*keys, dictionary, default=None):
    return [
        # The get() method returns the value of the item with the specified key
        dictionary.get(key, default)
        for key in keys
    ]


fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}

# The arguments dictionary and default come after *keys, which means they must be specified as keyword arguments.
result = get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown')
print(result)


