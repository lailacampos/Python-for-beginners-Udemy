# Serialization and the Pickle module
# https://realpython.com/python-pickle-module/#serialization-in-python

# The serialization process is a way to convert a data structure into a linear form that can be stored or
# transmitted over a network.
# This process is also referred to as marshalling.

# The reverse process, which takes a stream of bytes and converts it back into a data structure, is called
# deserialization or unmarshalling.

# The JSON format is human readable and language independent, and it’s lighter than XML.
# With the json module, you can serialize and deserialize several standard Python types.

# The pickle module differs from the json module in that it serializes objects in a binary format, which means the
# result is not human readable.
# However, it’s also faster and it works with many more Python types right out of the box, including
# custom-defined objects.

import pickle


class ExampleClass:
    a_number = 35
    a_string = 'Hello'
    a_list = [1, 2, 3]
    a_dict = {1: 'one', 2: 'two', 123: [1, 2, 3]}
    a_tuple = (4, 5, 6)


obj = ExampleClass()

# dumps() creates a string
pickled_obj = pickle.dumps(obj)
print(f'This is my serialized object: {pickled_obj}')

unpickled_obj = pickle.loads(pickled_obj)
print(f'This is my un-serialized object: {unpickled_obj}')
print(unpickled_obj.a_dict)
