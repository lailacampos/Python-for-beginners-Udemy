# Combining <flag> Arguments in a Function Call
# https://realpython.com/regex-python/#combining-flags-arguments-in-a-function-call

import re

# Flag values are defined so that you can combine them using the bitwise OR (|) operator.
# This allows you to specify several flags in a single function call:

print(re.search('^bar', 'FOO\nBAR\nBAZ', re.IGNORECASE | re.MULTILINE))  # match = 'BAR'

######################################################################################

# Setting and Clearing Flags Within a Regular Expression

# In addition to being able to pass a <flags> argument to most re module function calls, you can also modify flag values within a regex in Python.

######################################################################################

# (?<flags>)
# Sets flag value(s) for the duration of a regex.

# Within a regex, the metacharacter sequence (?<flags>) sets the specified flags for the entire expression.
# The value of <flags> is one or more letters from the set a, i, L, m, s, u, and x.

# a	    re.A     re.ASCII
# i	    re.I     re.IGNORECASE
# L	    re.L     re.LOCALE
# m	    re.M     re.MULTILINE
# s	    re.S     re.DOTALL
# u	    re.U     re.UNICODE
# x	    re.X     re.VERBOSE

# The (?<flags>) metacharacter sequence as a whole matches the empty string. It always matches successfully and doesn’t consume any of the search
# string.

# The following examples are equivalent:
print(re.search('^bar', 'FOO\nBAR\nBAZ', re.I|re.M))  # match = 'BAR'
print(re.search('(?im)^bar', 'FOO\nBAR\nBAZ'))  # match = 'BAR'

# A (?<flags>) metacharacter sequence sets the given flag(s) for the entire regex no matter where you place it in the expression:
print(re.search('foo.bar(?s).baz', 'foo\nbar\nbaz'))  # match = 'foo\nbar\baz'

# However, as of Python 3.7, it’s deprecated to specify (?<flags>) anywhere in a regex other than at the beginning.
# It still produces the appropriate match, but it displays a warning message.

######################################################################################

# (?<set_flags>-<remove_flags>:<regex>)
# Sets or removes flag value(s) for the duration of a group.

# (?<set_flags>-<remove_flags>:<regex>) defines a non-capturing group that matches against <regex>.
# For the <regex> contained in the group, the regex parser sets any flags specified in <set_flags> and clears any flags specified in <remove_flags>.

# Values for <set_flags> and <remove_flags> are most commonly i, m, s or x.

# In the following example, the IGNORECASE flag is set for the specified group.
# This produces a match because (?i:foo) dictates that the match against 'FOO' is case insensitive.
print(re.search('(?i:foo)bar', 'FOObar'))  # match = 'FOObar'

# Now contrast that with this example:
# Outside the group, IGNORECASE is no longer in effect, so the match against 'BAR' is case sensitive and fails.
print(re.search('(?i:foo)bar', 'FOOBAR'))  # None

# Turning a flag off for a group:
# Although re.IGNORECASE enables case-insensitive matching for the entire call, the metacharacter sequence (?-i:foo) turns off IGNORECASE for
# the duration of that group, so the match against 'FOO' fails.
print(re.search('(?-i:foo)bar', 'FOOBAR', re.IGNORECASE))  # None
