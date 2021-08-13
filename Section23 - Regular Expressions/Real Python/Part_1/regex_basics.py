# Regular Expressions or Regex basics
# https://realpython.com/regex-python/
# https://realpython.com/regex-python-part-2/

# A regular expression (shortened as regex or regexp) is a sequence of characters that specifies a search pattern.
# A regex is a special sequence of characters that defines a pattern for complex string-matching functionality.

# Regex functionality in Python resides in a module named re.
import re

str = 'foo123bar'

# re.search(<regex>, <string>)
# re.search(<regex>, <string>) scans <string> looking for the first location where the pattern <regex> matches.
# If a match is found, then re.search() returns a match object. Otherwise, it returns None.
# search() scans the search string from left to right, and as soon as it locates a match for <regex>,
# it stops scanning and returns the match.
match = re.search('123', str)

# A match object is truthy (a value that is True in a boolean context).
print(match.span().index(3))
