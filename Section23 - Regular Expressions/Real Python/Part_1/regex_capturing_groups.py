# Capturing groups
# https://realpython.com/regex-python/#capturing-groups

# Most (but not quite all) grouping constructs also capture the part of the search string that matches the group.
# You can retrieve the captured portion or refer to it later in several different ways.

# There are two methods defined for a match object that provide access to captured groups: .groups() and .group().

# m.groups() -> Returns a tuple containing all the captured groups from a regex match.

import re

# + Matches one or more repetitions of the preceding regex.
# Each of the three (\w+) expressions matches a sequence of word characters.
# The full regex (\w+),(\w+),(\w+) breaks the search string into three comma-separated tokens.
m = re.search('(\w+),(\w+),(\w+)', 'foo,quiz,baz')
print(m)

# Because the (\w+) expressions use grouping parentheses, the corresponding matching tokens are captured.
# To access the captured matches, you can use .groups(), which returns a tuple containing all the captured matches in order:
print(m.groups())  # ('foo', 'quux', 'baz')

# the tuple contains the tokens but not the commas that appeared in the search string.
# That’s because the word characters that make up the tokens are inside the grouping parentheses but the commas aren't.

######################################################################################

# m.group(<n>)
# Returns a string containing the <n>th captured match.

# With one argument, .group() returns a single captured match.
# The arguments are one-based, not zero-based.
# So, m.group(1) refers to the first captured match, m.group(2) to the second, and so on.
print(m.group(1))  # foo
print(m.group(2))  # quux

# m.group(0) returns the entire match, and m.group() does the same.
print(m.group())  # foo,quux,baz
print(m.group(0))  # foo,quux,baz

######################################################################################

# m.group(<n1>, <n2>, ...)
# Returns a tuple containing the specified captured matches.

# With multiple arguments, .group() returns a tuple containing the specified captured matches in the given order.
print(m.group(2, 3))  # ('quux', 'baz')
print(m.group(3, 2, 1))  # ('baz', 'quux', 'foo')
