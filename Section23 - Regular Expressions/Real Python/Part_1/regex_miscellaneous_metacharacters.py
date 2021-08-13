# Miscellaneous Metacharacters
# https://realpython.com/regex-python/#miscellaneous-metacharacters

import re

# (?#...)
# Specifies a comment.
# The regex parser ignores anything contained in the sequence (?#...)

# * metacharacter
# Matches zero or more repetitions of the preceding regex.
print(re.search('bar(?#This is a comment)-*foo', 'bar--foo-bar'))  # match = 'bar--foo'

######################################################################################

# Vertical bar, or pipe (|)
# Specifies a set of alternatives on which to match.

# An expression of the form <regex_1>|<regex_2>|...|<regex_n> matches at most one of the specified <regex_i> expressions.

# foo|bar|baz will match any of 'foo', 'bar', or 'baz'.
# It's possible to separate any number of regexes using |.
print(re.search('foo|bar|quiz', 'foo'))  # match = 'foo'
print(re.search('foo|bar|quiz', 'bar'))  # match = 'bar'
print(re.search('foo|bar|quiz', 'quiz'))  # match = 'quiz'

# Alternation is non-greedy.
# The regex parser looks at the expressions separated by | in left-to-right order and returns the first match that it finds.
# The remaining expressions aren’t tested, even if one of them would produce a longer match:

# In this case, the pattern specified on line 6, 'foo|barquiz', would match on either 'foo' or 'barquiz'.
# The match returned is 'foo' because that appears first when scanning from left to right, even though 'barquiz' would be a longer match.
print(re.search('foo|barquiz', 'foo barquiz'))

######################################################################################


