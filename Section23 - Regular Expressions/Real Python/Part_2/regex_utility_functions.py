# Utility Functions
# https://realpython.com/regex-python-part-2/#utility-functions

# re.split()	    Splits a string into substrings using a regex as a delimiter
# re.escape()	    Escapes characters in a regex

import re

# re.split(<regex>, <string>, maxsplit=0, flags=0)
# Splits a string into substrings.

# re.split(<regex>, <string>) splits <string> into substrings using <regex> as the delimiter and returns the substrings as a list.

# Splits the specified string into substrings delimited by a comma (,), semicolon (;), or slash (/) character, surrounded by any amount of whitespace
regex = r'''
                \s*          # Optional whitespace
                [,;/-]      # Delimiters
                \s*          # Optional whitespace
                
                '''

print(re.split(regex, 'foo-bar , quiz  ; baz ', flags=re.VERBOSE))  # ['foo', 'bar', 'quiz', 'baz ']

# If <regex> contains capturing groups, then the return list includes the matching delimiter strings as well:
print(re.split('(\s*[,;/-]\s*)', 'foo-bar , quiz  ; baz '))  # ['foo', '-', 'bar', ' , ', 'quiz', '  ; ', 'baz ']

# Split <string> apart into delimited tokens, process the tokens in some way, then piece the string back together using the same delimiters that
# originally separated them:

string = 'foo,bar  ;  baz / quiz'
regex = r'(\s*[,;/-]\s*)'
a = re.split(regex, string)  # a = ['foo', ',', 'bar', '  ;  ', 'baz', ' / ', 'qux']

# Enclose each token in <>'s
for i, s in enumerate(a):

    # Will be True for the tokens but not the delimiters.
    # As in the delimiters will match, but the words won't. So enclose that which doesn't match.
    if not re.fullmatch(regex, s):
        a[i] = f'<{s}>'
        print(a[i])  # [<foo>, <bar>, <baz>, <quiz>]

a = ''.join(a)
print(a)  # <foo>,<bar>  ;  <baz> / <quiz>

######################################################################################

# re.escape(<regex>)
# Escapes characters in a regex.

# re.escape(<regex>) returns a copy of <regex> with each nonword character (anything other than a letter, digit, or underscore) preceded by a
# backslash.

# It's useful if you’re calling one of the re module functions, and the <regex> you’re passing in has a lot of special characters that you want
# the parser to take literally instead of as metacharacters.

print(re.match('foo^bar(baz)|quiz', 'foo^bar(baz)|quiz'))  # None

# Escaping with \ character:
print(re.match('foo\^bar\(baz\)\|quiz', 'foo^bar(baz)|quiz'))  # match = 'foo^bar(baz)|quiz'

# Using re.escape():
print(re.match(re.escape('foo^bar(baz)|quiz'), 'foo^bar(baz)|quiz'))  # match = 'foo^bar(baz)|quiz'


