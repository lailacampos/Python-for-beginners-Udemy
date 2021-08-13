# Lookahead and Lookbehind Assertions
# https://realpython.com/regex-python/#lookahead-and-lookbehind-assertions

# Lookahead and lookbehind assertions determine the success or failure of a regex match in Python based on what is just behind (to the left) or
# ahead (to the right) of the parser’s current position in the search string.

# Like anchors, lookahead and lookbehind assertions are zero-width assertions, so they don’t consume any of the search string.
# Also, even though they contain parentheses and perform grouping, they don’t capture what they match.

import re

# (?=<lookahead_regex>)
# Creates a positive lookahead assertion.

# (?=<lookahead_regex>) asserts that what follows the regex parser’s current position must match <lookahead_regex>.

# Example 1:
# The lookahead assertion (?=[a-z]) specifies that what follows 'foo' must be a lowercase alphabetic character.
# In the case above, it’s the character 'b', so a match is found.
print(re.search('foo(?=[a-z])', 'foobar'))  # match = 'foo'

# Example 2:
# The next character after 'foo' is '1', so there isn’t a match. The lookahead fails.
print(re.search('foo(?=[a-z])', 'foo123'))  # None

# What’s unique about a lookahead is that the portion of the search string that matches <lookahead_regex> isn’t consumed,
# and it isn’t part of the returned match object.
# The regex parser looks ahead only to the 'b' that follows 'foo' but doesn't pass over it yet.
# You can tell that 'b' isn’t considered part of the match because the match object displays match='foo'.

# As opposed to:
# This time, the regex consumes the 'b', and it becomes a part of the eventual match.
print(re.search('foo([a-z])', 'foobar'))  # match = 'foob'

######################################################################################

# (?!<lookahead_regex>)
# Creates a negative lookahead assertion.

# (?!<lookahead_regex>) asserts that what follows the regex parser’s current position must NOT match <lookahead_regex>.

# The negative lookahead assertions on lines 3 and 8 stipulate that what follows 'foo' should not be a lowercase alphabetic character.
print(re.search('foo(?![a-z])', 'foobar'))  # None

print(re.search('foo(?![a-z])', 'foo123'))  # match = 'foo'

######################################################################################

# (?<=<lookbehind_regex>)
# Creates a positive lookbehind assertion.

# (?<=<lookbehind_regex>) asserts that what precedes the regex parser’s current position must match <lookbehind_regex>.

# In the following example, the lookbehind assertion specifies that 'foo' must precede 'bar'
print(re.search('(?<=foo)bar', 'foobar'))  # match = 'bar'

# This example fails to match because the lookbehind requires that 'qux' precede 'bar':
print(re.search('(?<=quiz)bar', 'foobar'))  # None

# Unlike the <lookahead_regex>, the <lookbehind_regex> in a lookbehind assertion must specify a match of fixed length.
# For example, the following isn’t allowed because the length of the string matched by a+ is indeterminate:
# print(re.search('(?<=a+)def', 'aaadef'))

# This, however, is okay:
# Anything that matches a{3} will have a fixed length of three, so a{3} is valid in a lookbehind assertion.
print(re.search('(?<=a{3})def', 'aaadef'))  # match = 'def'

######################################################################################

# (?<!--<lookbehind_regex-->)
# Creates a negative lookbehind assertion.

# (?<!<lookbehind_regex>) asserts that what precedes the regex parser’s current position must not match <lookbehind_regex>.
print(re.search('(?<!quiz)bar', 'foobar'))  # match = 'bar'

print(re.search('(?<!quiz)bar', 'quizbar'))  # None

