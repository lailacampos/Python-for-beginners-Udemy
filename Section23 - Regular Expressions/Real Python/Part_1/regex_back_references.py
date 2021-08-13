# Back references
# https://realpython.com/regex-python/#backreferences

import  re

# \<n>
# Matches the contents of a previously captured group.

# Within a regex in Python, the sequence \<n>, where <n> is an integer from 1 to 99, matches the contents of the <n>th captured group.

# (\w+) matches the first instance of the string 'foo' and saves it as the first captured group.
# The comma matches literally.
# Then \1 is a back reference to the first captured group and matches 'foo' again.
regex = r'(\w+),\1'
print(re.search(regex, 'foo,foo'))  # match='foo,foo'

# The bellow doesn't have a match because what comes before the comma isn’t the same as what comes after it, so the \1 back reference doesn't match.
print(re.search(regex, 'foo,bar'))  # None
