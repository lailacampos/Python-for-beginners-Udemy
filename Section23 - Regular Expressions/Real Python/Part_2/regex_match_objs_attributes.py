# Match Object Attributes
# https://realpython.com/regex-python-part-2/#match-object-attributes

import re

# match.pos
# match.endpos
# Contain the effective values of <pos> and <endpos> for the search.

# Some methods, when invoked on a compiled regex, accept optional <pos> and <endpos> arguments that limit the search to a portion of the
# specified search string.
# These values are accessible from the match object with the .pos and .endpos attributes

re_obj = re.compile(r'\d+')
match = re_obj.search('foo123bar', 2, 7)
print(match)  # match = '123'
print(match.pos, ',', match.endpos)  # 2 , 7

# If the <pos> and <endpos> arguments aren’t included in the call, either because they were omitted or because the function in question doesn’t
# accept them, then the .pos and .endpos attributes effectively indicate the start and end of the string.
match = re_obj.search('foo123bar')
print(match.pos, '-', match.endpos)  # 0 - 9

######################################################################################

# match.lastindex
# Contains the index of the last captured group.

# match.lastindex is equal to the integer index of the last captured group.
match = re.search(r'(\w+)-(\w+)-(\w+)', 'foo-123-bar')
print(match)  # match = 'foo-123-bar'
print(match.lastindex)  # 3
print(match[match.lastindex])  # bar

# In cases where the regex contains potentially nonparticipating groups, this allows for determining how many groups actually participated in the
# match.
match = re.search(r'(\w+)-(\w+)-?(\w+)?', 'foo-123')
print(match) # match = 'foo-123-'
print(match.groups())  # ('foo', '123', None)

# The third group, which is optional because of the question mark (?) metacharacter, does participate in the match.
print(match.lastindex, '-', match[match.lastindex])  # 2 - 123

######################################################################################

# match.lastgroup
# Contains the name of the last captured group.

# If the last captured group originates from the (?P<name><regex>) metacharacter sequence, then match.lastgroup returns the name of that group.
match = re.search(r'(?P<num1>\d+)\D*(?P<num2>\d+)', 'foo123bar456quiz')
print(match.lastgroup)  # num2

# match.lastgroup returns None if the last captured group isn’t a named group
match = re.search(r'(\d+)\D*(\d+)', 'foo-123-bar-456-quiz')
print(match.groups())  # ('123', '456')
print(match.lastgroup)  # None

######################################################################################

# match.re
# Contains the regular expression object for the match.

# match.re contains the regular expression object that produced the match.
# This is the same object you’d get if you passed the regex to re.compile().
match = re.search(r'(\w+)-(\w+)-(\w+)', 'foo-123-bar')
print(match.re)  # re.compile('(\\w+)-(\\w+)-(\\w+)')

# It's possible to access all of that object’s attributes as well:
print(match.re.groups)  # 3
print(match.re.pattern)  # (\w+)-(\w+)-(\w+)

# It's also possible to invoke any of the methods defined for a compiled regular expression object on it:
match = re.search(r'(\w+)-(\w+)-(\w+)', 'foo-bar-quiz')
print(match.re)  # re.compile('(\\w+)-(\\w+)-(\\w+)')

# Here .match() is invoked on m.re to perform another search using the same regex but on a different search string:
print(match.re.match('quiz-baz-foo'))  # natch = 'quiz-baz-foo'

######################################################################################

# match.string
# Contains the search string for a match.

# match.string contains the search string that is the target of the match:
match = re.search(r'(\w+)-(\w+)-(\w+)', 'foo-bar-quiz')
print(match.string)  # foo-bar-quiz
