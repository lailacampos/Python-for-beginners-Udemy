# Compiled Regex Objects in Python
# https://realpython.com/regex-python-part-2/#compiled-regex-objects-in-python

import re

# re.compile(<regex>, flags=0)
# Compiles a regex into a regular expression object.

# re.compile(<regex>) compiles <regex> and returns the corresponding regular expression object.
# If a <flags> value is included, then the corresponding flags apply to any searches performed with the object.

# There are two ways to use a compiled regular expression object.
# Specifying it as the first argument to the re module functions in place of <regex>:

# re_obj = re.compile(<regex>, <flags>)
re_obj = re.compile(r'\w+', re.IGNORECASE)

# result = re.search(re_obj, <string>)
result = re.search(re_obj, 'aaBcDe')
print(result)  # match = 'aaBcDe'

# It's also possible to invoke a method directly from a regular expression object:
# result = re_obj.search(<string>)
result = re_obj.search('aaBcDe')
print(result)  # match = 'aaBcDe'

# Both of the examples above are equivalent to this:
# result = re.search(<regex>, <string>, <flags>)
result = re.search(r'\w+', 'aaBcDe', re.IGNORECASE)
print(result)  # match = 'aaBcDe'

######################################################################################

# Regular Expression Object Attributes
# https://realpython.com/regex-python-part-2/#regular-expression-object-attributes

# The re module defines several useful attributes for a compiled regular expression object:

# re_obj.flags	        Any <flags> that are in effect for the regex
re_obj = re.compile(r'(?m)(\w+)(\w+)', re.IGNORECASE)
print(re_obj.flags)  # 42

# In the regular expression object defined above there are three flags defined:
# re.IGNORECASE: Specified as a <flags> value in the re.compile() call
# re.M: Specified as (?m) within the regex
# re.UNICODE: Enabled by default

# The value of re_obj.flags is the logical OR of these three values, which equals 42.

# re_obj.groups	        The number of capturing groups in the regex
print(re_obj.groups)  # 2

# re_obj.pattern	    The <regex> pattern that produced this object
print(re_obj.pattern)  # (?m)(\w+)(\w+)

# re_obj.groupindex	    A dictionary mapping each symbolic group name defined by the (?P<name>) construct (if any) to the corresponding group number
re_obj = re.compile(r'(?P<w1>),(?P<w2>)')
print(re_obj.groupindex)  # {'w1': 1, 'w2': 2}
print(re_obj.groupindex['w1'])  # 1
print(re_obj.groupindex['w2'])  # 2


