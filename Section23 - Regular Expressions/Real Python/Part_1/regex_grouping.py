# Grouping Constructs and Backreferences
# https://realpython.com/regex-python/#grouping-constructs-and-backreferences

# 1 - Grouping: A group represents a single syntactic entity. Additional metacharacters apply to the entire
# group as a unit.
# 2 - Capturing: Some grouping constructs also capture the portion of the search string that matches the subexpression
# in the group. You can retrieve captured matches later through several different mechanisms.

import re

# (<regex>) Defines a subexpression or group.
# In this example, 'bar' and '(bar)' mean the same thing:
print(re.search('(bar)', 'foo bar foo'))  # Returns a match
print(re.search('bar', 'foo bar foo'))  # Returns a match

######################################################################################

# Treating a Group as a Unit
# https://realpython.com/regex-python/#treating-a-group-as-a-unit

# A quantifier metacharacter that follows a group operates on the entire subexpression specified in the group
# as a single unit.
# '(bar)+' =  Matches one or more occurrences of 'bar' (greedy)
print(re.search('(bar)+', 'foo bar baz'))  # match = 'bar'
print(re.search('(bar)+', 'foo barbar baz'))  # match = 'barbar'
print(re.search('(bar)+', 'foo barbarbar baz'))  # match = 'barbarbar'

# 'bar+' -> The + metacharacter applies only to the character 'r'. -> 'ba' followed by one or more occurrences of 'r'
# Ex: 'bar', 'barr', 'barrr'

# '(bar)+' -> The + metacharacter applies to the entire string 'bar'. -> One or more occurrences of 'bar'
# Ex: 'bar', 'barbar', 'barbarbar'

# A more complicate example:
# '(ba[rz]){2,4}(qux)?' = Matches 2 to 4 occurences of either 'bar' or 'baz', optionally followed by 'qux'
print(re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux'))  # match = 'bazbarbazqux'
print(re.search('(ba[rz]){2,4}(qux)?', 'barbar'))  # match = 'barbar'

# Another complicated example:
# '(foo(bar)?)+(\d\d\d)?'

# foo(bar)? = 'foo' optionally followed by 'bar'
# (foo(bar)?)+ = One or more occurrences of the above
# \d\d\d = Three decimal digit characters
# (\d\d\d) = Zero or one occurrences of the above

# '(foo(bar)?)+(\d\d\d)?' = String it all together and you get: at least one occurrence of 'foo' optionally followed by
#                           'bar', all optionally followed by three decimal digit characters.
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123'))  # match = 'foofoobar123'
