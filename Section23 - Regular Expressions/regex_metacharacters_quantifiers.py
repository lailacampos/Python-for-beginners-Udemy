# Regex Metacharacters - Quantifiers
# https://realpython.com/regex-python/#quantifiers

# A quantifier metacharacter immediately follows a portion of a <regex> and indicates how many times that portion
# must occur for the match to succeed.

# For example, a* matches zero or more 'a' characters. That means it would match an empty string, 'a', 'aa',
# 'aaa', and so on.

import re

# * metacharacter

print(re.search('foo-*bar', 'foobar'))  # Returns a match because there are 0 '-' characters between 'foo' and 'bar'
print(re.search('foo-*bar', 'foo-bar'))  # Returns a match because there are 1 '-' characters between 'foo' and 'bar'
print(re.search('foo-*bar', 'foo--bar'))  # Returns a match because there are 2 '-' characters between 'foo' and 'bar'

# The metacharacter sequence -* matches in all three cases.

# .*
# .* Matches zero or more occurrences of any character. It matches any character sequence up to a line break.
# .* matches everything between 'foo' and 'bar':
print(re.search('foo.*bar', 'foo q9sa90)*867 bar #$')) # Returns a match

######################################################################################

# + metacharacter
# + Matches one or more repetitions of the preceding regex.
# + is similar to * but the quantified regex must occur at least once

print(re.search('foo-+bar', 'foobar'))  # Returns None because there are 0 '-' characters between 'foo' and 'bar'
print(re.search('foo-+bar', 'foo-bar'))  # Returns a match because there are 1 '-' characters between 'foo' and 'bar'
print(re.search('foo-+bar', 'foo--bar'))  # Returns a match because there are 2 '-' characters between 'foo' and 'bar'

######################################################################################

# ? metacharacter
# ? Matches zero or one repetitions of the preceding regex.
# It's similar to * and +, but in this case there’s only a match if the preceding regex occurs once or not at all.

print(re.search('foo-?bar', 'foobar'))  # Returns a match because there are 0 '-' characters between 'foo' and 'bar'
print(re.search('foo-?bar', 'foo-bar'))  # Returns a match because there are 1 '-' characters between 'foo' and 'bar'
print(re.search('foo-?bar', 'foo--bar'))  # Returns None because there are 2 '-' characters between 'foo' and 'bar'

######################################################################################
# When used alone, the quantifier metacharacters *, +, and ? are all greedy, meaning they produce the longest
# possible match.
# The regex <.*> means:
# 1 - A '<' character
# 2 - Then any sequence of characters
# 3 - Then a '>' character

# Consider the example:
print(re.search('<.*>', '%<foo> <bar> <baz>'))  # In this case the match ends with the '>' character following 'baz'

# <.*> matches the first '<' character and then the LAST '>' character

# *?
# To be able to get the shortest possible match instead, then use the non-greedy metacharacter sequence *?:
print(re.search('<.*?>', '%<foo> <bar <baz>>')) # In this case the match ends with the '>' character following 'foo'

# +?
# '<.+?>' = There must be at least one alphanumeric character between '<' and the shortest '>'.
print(re.search('<.+?>', '<> ')) # Returns None

######################################################################################

# {m}
# {m} Matches exactly m repetitions of the preceding regex.
# It's similar to * or +, but it specifies exactly how many times the preceding regex must occur for a match to succeed.

print(re.search('x-{3}x', 'x--x'))  # Returns None because there are not exactly three '-' characters between x and x
print(re.search('x-{3}x', 'x---x'))  # Returns a match because there are exactly three '-' characters between x and x
print(re.search('x-{3}x', 'x------x'))  # Returns None because there are not exactly three '-' characters

######################################################################################

# {m,n}
# {m,n} Matches any number of repetitions of the preceding regex from m to n, inclusive.
# Ex: the quantified <regex> 'x-{2,4}x' succeeds when there are two, three, or four dashes between the 'x'
# characters but fails otherwise

for i in range(1,6):
    s = f"x{'-' * i}x"
    print(f'{i} {s:10}', re.search('x-{2,4}x', s))

# Prints:
# 1 x-x        None
# 2 x--x       <re.Match object; span=(0, 4), match='x--x'>
# 3 x---x      <re.Match object; span=(0, 5), match='x---x'>
# 4 x----x     <re.Match object; span=(0, 6), match='x----x'>
# 5 x-----x    None

# <regex>{,n} = <regex>{0,n} = Any number of repetitions of <regex> less than or equal to n
# <regex>{m,}	Any number of repetitions of <regex> greater than or equal to m
# <regex>{,} = <regex>{0,}<regex>* = Any number of repetitions of <regex>

# If m, n and the comma are ommited, then the curly braces no longer function as metacharacters.
# {} matches just the literal string '{}'
print(re.search('x{}x', 'x{}x')) # Returns a match

# If it's not one of the following:
# {m,n}
# {m,}
# {,n}
# {,}
# Then the regex will match literally.
print(re.search('x{foo}x', 'x{foo}x'))  # Returns a match

# {m,n}?
# {m,n}? Will return the shortest possible match while {m,n} will return the longest possible match.
# Examples:
print(re.search('a{3,5}', 'aaaaaaaaaa'))  # Will match 'aaaaa', the longest possible match
print(re.search('a{3,5}', 'aaaaaaaaaa'))  # Will match 'aaa', the shortest possible match

