# Match Object Methods
# https://realpython.com/regex-python-part-2/#match-object-methods-and-attributes

import re

# Match Object Methods

# match.group([<group1>, ...])
# Returns the specified captured group(s) from a match.

# For numbered groups, match.group(n) returns the nth group:
match = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

# Remember: Numbered captured groups are one-based, not zero-based.
print(match.group(1))  # foo
print(match.group(2))  # bar

# With more than one argument, .group() returns a tuple of all the groups specified.
# A given group can appear multiple times, and you can specify any captured groups in any order:
print(match.group(1, 2, 3, 3, 2, 1))  # ('foo', 'bar', 'baz', 'baz', 'bar', 'foo')

# It can also happen that a group participates in the overall match multiple times.
# If you call .group() for that group number, then it returns only the part of the search string that matched the last time.
# The earlier matches aren’t accessible.
match = re.match(r'(\w{3},)+', 'foo,bar,baz,quiz')
print(match)  # match = 'foo,bar,baz,'
print(match.group(1))  # baz,

######################################################################################

# match.__getitem__(<grp>)
# Returns a captured group from a match.

# match.__getitem__(<grp>) is identical to match.group(<grp>) and returns the single group specified by <grp>
match = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(match.group(2))  # bar
print(match.__getitem__(2))  # bar

######################################################################################

# match.groups(default=None)
# Returns all captured groups from a match.

# match.groups() returns a tuple of all captured groups:
print(match.groups())  # ('foo', 'bar', 'baz')

# when a group in a regex in Python doesn’t participate in the overall match, .group() returns None for that group.
# By default, .groups() does likewise.

# To return something else in this situation, use the default keyword argument.
match = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
print(match.group(3))  # None
print(match.groups(default='---'))  # ('foo', 'bar', '---')

######################################################################################

# match.groupdict(default=None)
# Returns a dictionary of named captured groups.

# match.groupdict() returns a dictionary of all named groups captured with the (?P<name><regex>) metacharacter sequence.
# The dictionary keys are the group names and the dictionary values are the corresponding group values.

match = re.search(r'(?P<w1>\w+),bar,quiz,(?P<w2>\w+)', 'foo,bar,quiz,baz')
print(match.groupdict())  # {'w1': 'foo', 'w2': 'baz'}
print(match.groupdict()['w2'])  # baz

# As with .groups(), for .groupdict() the default argument determines the return value for nonparticipating groups.
match = re.search(r'foo,(?P<w1>\w+),bar,(?P<w2>\w+)?', 'foo,baz,bar,,quiz')
print(match.groupdict())  # {'w1': 'baz', 'w2': None}
print(match.groupdict(default='---'))  # {'w1': 'baz', 'w2': '---'}

######################################################################################

# match.expand(<template>)
# Performs backreference substitutions from a match.

# match.expand(<template>) returns the string that results from performing back reference substitution on <template> exactly as re.sub() would do.
match = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,quiz')
print(match.groups())  # ('foo', 'bar', 'quiz')

print(match.expand(r'\2'))  # bar
print(match.expand(r'[\3] -> [\1]'))  # [quiz] -> [foo]

match = re.search(r'(?P<num>\d+)', 'foo123quiz')
print(match.group(1))  # 123
print(match.expand(r'--- \g<num> ---'))  # --- 123 ---

######################################################################################

# match.start([<grp>])
# match.end([<grp>])
# Return the starting and ending indices of the match.

# match.start() returns the index in the search string where the match begins.
# match.end() returns the index immediately after where the match ends.
string = 'foo123bar456quiz'
match = re.search(r'\d+', string)
print(match)  # match = '123'

# It's possible to slice the string:
print(string[match.start():match.end()])  # 123

# match.start(<grp>) and match.end(<grp>) return the starting and ending indices of the substring matched by <grp>, which may be a numbered or
# named group.

# One or more digits followed by zero or more of any non-digit character, followed by one or more digits
match = re.search(r'(\d+)\D*(?P<num>\d+)', string)
print(match)  # match = '123bar456'
print(match.group(1))  # 123
print(match.start(1), ',', match.end(1)) # 3, 6

print(match.group('num'))  # 456
print(match.start('num'), ',', match.end('num'))  # 9 , 12

# If the specified group matches a null string, then .start() and .end() are equal:
match = re.search(r'foo-(\d*)bar', 'foo-bar')
print(match)  # match = 'foo-bar'
print(match.groups())  # ('',)
print(match[1])  # empty string
print(match[0])  # foo-bar
print(match.start(1), ',', match.end(1))  # 4 , 4

######################################################################################

# match.span([<grp>])
# Returns both the starting and ending indices of the match.

# match.span() returns both the starting and ending indices of the match as a tuple.
# If you specified <grp>, then the return tuple applies to the given group.

# One or more digits followed by zero or more of any non-digit character, followed by one or more digits
match = re.search(r'(\d+)\D*(?P<num>\d+)', 'foo123bar456baz')
print(match)  # match = '123bar456'

# Full match
print(match[0])  # 123bar456
print(match[1])  # 123
print(match[2])  # 456
print(match['num'])  # 456

print(match.span(1))  # (3, 6)
print(match.span('num'))  # (9, 12)

# The following are equivalent:
# match.span(<grp>)
# (match.start(<grp>), match.end(<grp>))
print(match.start('num'), ',', match.end('num'))  # 9 , 12
# match.span() just provides a convenient way to obtain both match.start() and match.end() in one method call.
