# Other Grouping Constructs
# https://realpython.com/regex-python/#other-grouping-constructs

import re

# (?P<name><regex>)
# Creates a named captured group.

# This metacharacter sequence is similar to grouping parentheses in that it creates a group matching <regex> that is accessible through the match
# object or a subsequent back reference.
# The difference in this case is that you reference the matched group by its given symbolic <name> instead of by its number.

# Example with three captured groups numbered 1, 2, and 3:
m = re.search('(\w+),(\w+),(\w+)', 'foo,quiz,bar')
print(m.groups())  # ('foo', 'quiz', 'bar')
print(m.group(1, 2, 3))  # ('foo', 'quiz', 'bar')

# The following does the same thing as the above except that the groups have the symbolic names w1, w2, and w3.
# Each <name> can only appear once per regex.
m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quiz,bar')
print(m.group('w1', 'w2', 'w3'))  # ('foo', 'quiz', 'bar')

######################################################################################

# (?P=<name>)
# Matches the contents of a previously captured named group.

# The (?P=<name>) metacharacter sequence is a back reference, similar to \<n>, except that it refers to a named group rather than a numbered group.

# (\w+) matches the first instance of the string 'foo' and saves it as the first captured group.
# The comma matches literally.
# Then \1 is a back reference to the first captured group and matches 'foo' again.
m = re.search(r'(\w+),\1', 'foo,foo')
print(m)  # match = 'foo,foo'

# (?P=<word>\w+) matches 'foo' and saves it as a captured group named word.
# The comma matches literally.
# Then (?P=word) is a back reference to the named capture and matches 'foo' again
m = re.search(r'(?P<word>\w+),(?P=word)', 'foo,foo')
print(m)  # match = 'foo,foo'

# Obs: The angle brackets (< and >) are required around name when creating a named group but not when referring to it later, either by
#       back reference or by .group()

######################################################################################

# (?:<regex>)
# Creates a non-capturing group.

# (?:<regex>) is just like (<regex>) in that it matches the specified <regex>. But (?:<regex>) doesn't capture the match for later retrieval.
m = re.search('(\w+),(?:\w+),(\w+)', 'foo,quiz,bar')

# The middle word 'quiz' sits inside non-capturing parentheses, so it’s missing from the tuple of captured groups.
# It isn’t retrievable from the match object, nor would it be referable by back reference.
print(m.groups())  # ('foo', 'bar')

######################################################################################

# (?(<n>)<yes-regex>|<no-regex>)
# (?(<name>)<yes-regex>|<no-regex>)
# Specifies a conditional match.

# A conditional match matches against one of two specified regexes depending on whether the given group exists:

# (?(<n>)<yes-regex>|<no-regex>) matches against <yes-regex> if a group numbered <n> exists. Otherwise, it matches against <no-regex>.
# (?(<name>)<yes-regex>|<no-regex>) matches against <yes-regex> if a group named <name> exists. Otherwise, it matches against <no-regex>.

# Example:
regex = r'^(###)?foo(?(1)bar|baz)'

# Breakdown:
# ^(###)? indicates that the search string optionally begins with '###'.
#       If it does, then the grouping parentheses around ### will create a group numbered 1.
#       Otherwise, no such group will exist.
# foo literally matches the string 'foo'.
# (?(1)bar|baz) matches against 'bar' if group 1 exists
#       It matches against 'baz' if it doesn't.

# Example 1:
# The search string '###foobar' does start with '###', so the parser creates a group numbered 1.
# The conditional match is then against 'bar', which matches.
print(re.search(regex, '###foobar'))  # match = '###foobar'

# Example 2:
# The search string '###foobaz' does start with '###', so the parser creates a group numbered 1.
# The conditional match is then against 'bar', which doesn't match.
print(re.search(regex, '###foobaz'))  # None

# Example 3:
# The search string 'foobar' doesn't start with '###', so there isn’t a group numbered 1.
# The conditional match is then against 'baz', which doesn't match.
print(re.search(regex, 'foobar'))

# Example 4:
# The search string 'foobaz' doesn't start with '###', so there isn’t a group numbered 1.
# The conditional match is then against 'baz', which matches.
print(re.search(regex, 'foobaz'))  # match = 'foobaz'

######################################################################################

# Using a named group instead of a numbered group

regex = r'^(?P<char>\W)?foo(?(char)(?P=char)|)$'

# Breakdown:
# ^                     -> The start of the string.
# (?P<char>\W)          -> A single non-word character, captured in a group named char.
# (?P<char>\W)?         -> Zero or one occurrences of the above.
# foo                   -> The literal string 'foo'.
# (?(char)(?P=char)|)	-> The contents of the group named char if it exists, or the empty string if it doesn't.
# $                     -> The end of the string.

# If a non-word character precedes 'foo', then the parser creates a group named char which contains that character.
# The conditional match then matches against <yes-regex>, which is (?P=char), the same character again.
# That means the same character must also follow 'foo' for the entire match to succeed.

# If 'foo' isn’t preceded by a non-word character, then the parser doesn't create group char.
# <no-regex> is the empty string, which means there must not be anything following 'foo' for the entire match to succeed.
# Since ^ and $ anchor the whole regex, the string must equal 'foo' exactly.

# Example 1:
# 'foo' is by itself, so it matches.
print(re.search(regex, 'foo'))  # match = 'foo'

# Example 2:
# The same non-word character precedes and follows 'foo', so it matches.
print(re.search(regex, '#foo#'))  # match = '#foo#'

# Example 3:
# It doesn't match because it does not fulfill any of the conditions above.
print(re.search(regex, '@foo'))  # None

