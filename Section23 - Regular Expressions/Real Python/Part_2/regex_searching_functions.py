# Searching Functions
# https://realpython.com/regex-python-part-2/#searching-functions

# Searching functions scan a search string for one or more matches of the specified regex:

# re.search()	        Scans a string for a regex match
# re.match()	        Looks for a regex match at the beginning of a string
# re.fullmatch()	    Looks for a regex match on an entire string
# re.findall()	        Returns a list of all regex matches in a string
# re.finditer()	        Returns an iterator that yields regex matches from a string

import re

# re.search(<regex>, <string>, flags=0)
# Scans a string for a regex match.

# re.search(<regex>, <string>) looks for any location in <string> where <regex> matches:
# The function returns a match object if it finds a match and None otherwise.
print(re.search('\d+', 'foo123bar'))  # match = '123'
print(re.search(r'[a-z]+', '123-FOO-456', re.IGNORECASE))  # match = 'FOO'
print(re.search(r'\d+', 'foo.bar'))  # None

######################################################################################

# re.match(<regex>, <string>, flags=0)
# Looks for a regex match at the beginning of a string.

# This is identical to re.search(), except that re.search() returns a match if <regex> matches anywhere in <string>, whereas re.match()
# returns a match only if <regex> matches at the beginning of <string>.
print(re.match(r'\d+', '123foobar'))  # match = '123'
print(re.match(r'\d+', 'foo123bar'))  # None

# Warning:
# if <string> contains embedded newlines, then the MULTILINE flag causes re.search() to match the caret (^) anchor metacharacter either at the
# beginning of <string> or at the beginning of any line contained within <string>:
print(re.search('^foo', 'foo\nbar\nbaz'))  # match = 'foo'
print(re.search('^bar', 'foo\nbar\nbaz', re.MULTILINE))  # match = 'bar'

# The MULTILINE flag does not affect re.match() in this way.
# Even with the MULTILINE flag set, re.match() will match the caret (^) anchor only at the beginning of <string>, not at the beginning of lines
# contained within <string>.
print(re.match('^foo', 'foo\nbar\nbaz'))  # match = 'foo'
print(re.match('^bar', 'foo\nbar\nbaz'))  # None

######################################################################################

# re.fullmatch(<regex>, <string>, flags=0)
# Looks for a regex match on an entire string.

# This is similar to re.search() and re.match(), but re.fullmatch() returns a match only if <regex> matches <string> in its entirety.
print(re.fullmatch(r'\d+', 'foo123'))  # None
print(re.fullmatch(r'\d+', '123456'))  # match = '123456'

######################################################################################

# re.findall(<regex>, <string>, flags=0)
# Returns a list of all matches of a regex in a string.

# re.findall(<regex>, <string>) returns a list of all non-overlapping matches of <regex> in <string>.
# It scans the search string from left to right and returns all matches in the order found.
print(re.findall(r'\w+', '...foo,,,,bar:$%baz//'))  # match = ['foo', 'bar', 'baz']

# If <regex> contains a capturing group, then the return list contains only contents of the group, not the entire match.
# In this case, the specified regex is #(\w+)#. The matching strings are '#foo#', '#bar#', and '#baz#'.
# But the hash (#) characters don’t appear in the return list because they’re outside the grouping parentheses:
print(re.findall(r'#(\w+)#', '#foo#.#bar#.#baz#'))  # match = ['foo', 'bar', 'baz']

# If <regex> contains more than one capturing group, then re.findall() returns a list of tuples containing the captured groups.
# The length of each tuple is equal to the number of groups specified:
print(re.findall(r'(\w+),(\w+)', 'foo,bar,baz,quiz,laila,pineapple'))  # match = [('foo', 'bar'), ('baz', 'quiz'), ('laila', 'pineapple')]

# The above contains two capturing groups, so re.findall() returns a list of three two-tuples, each containing two captured matches.

######################################################################################

# re.finditer(<regex>, <string>, flags=0)
# Returns an iterator that yields regex matches.

# re.finditer(<regex>, <string>) scans <string> for non-overlapping matches of <regex> and returns an iterator that yields the match objects from
# any it finds.
# It scans the search string from left to right and returns matches in the order it finds them.
iterator = re.finditer(r'\w+', '...foo,,,,baz@#$%baz//|')
print(next(iterator))  # match = 'foo'
print(next(iterator))  # match = 'baz'
print(next(iterator))  # match = 'baz'

# Using for loop:
for i in re.finditer(r'\w+', '...foo,,,,baz@#$%baz//|'):
    print(i)

# re.findall() and re.finditer() are very similar, but they differ in two respects:
# re.findall() returns a list, whereas re.finditer() returns an iterator
#       The items in the list that re.findall() returns are the actual matching strings.
#       The items yielded by the iterator that re.finditer() returns are match objects.

