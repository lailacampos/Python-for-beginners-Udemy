# Regex Metacharacters - Anchors
# https://realpython.com/regex-python/#anchors

# Anchors are zero-width matches. They don’t match any actual characters in the search string, and they don’t
# consume any of the search string during parsing. Instead, an anchor dictates a particular location in the
# search string where a match must occur

import re

# ^ and \A
# Anchor a match to the start of <string>.

# When the regex parser encounters ^ or \A, the parser’s current position must be at the beginning of the search
# string for it to find a match.
print(re.search('\A123', '----123--'))  # Returns None because '123' is not at the beginning of the search string
print(re.search('^123', '123-----'))  # Returns a match object

######################################################################################

# $ and \Z
# When the regex parser encounters $ or \Z, the parser’s current position must be at the end of the search string
# for it to find a match. Whatever precedes $ or \Z must constitute the end of the search string.
print(re.search('abc$', 'abc-----'))  # Returns None because 'abc' is not at the end of the search string
print(re.search('abc\Z', '------abc'))  # Returns a match object

# As a special case, $ (but not \Z) also matches just before a single newline at the end of the search string.

######################################################################################

# \b and \B

# \b anchors a match to a word boundary.
# \b asserts that the regex parser’s current position must be at the beginning or end of a word.
# A word consists of a sequence of alphanumeric characters or underscores ([a-zA-Z0-9_]), the same as for the \w
# character class

print(re.search(r'\bbar', 'foo bar123'))  # Returns a match object because bar is at the beginning of a word
print(re.search(r'bar\b', 'foo bar123'))  # Returns None because bar is not at the end of a word.

# \B anchors a match to a location that isn’t a word boundary.
# \B does the opposite of \b. It asserts that the regex parser’s current position must not be at the start or end
# of a word.

print(re.search(r'\Bbar\B', '123 bar 456'))  # Returns None because bar IS at the beginning and/or end of a word
print(re.search(r'\Bbar\B', '123bar456'))  # Returns a match object
