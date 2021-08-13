# Substitution Functions
# https://realpython.com/regex-python-part-2/#substitution-functions

# Substitution functions replace portions of a search string that match a specified regex.

# re.sub()	    Scans a string for regex matches, replaces the matching portions of the string with the specified replacement string,
#               and returns the result.

# re.subn()	    Behaves just like re.sub() but also returns information regarding the number of substitutions made.

# Both re.sub() and re.subn() create a new string with the specified substitutions and return it.
# The original string remains unchanged.

######################################################################################

import re

# re.sub(<regex>, <repl>, <string>, count=0, flags=0)
# Returns a new string that results from performing replacements on a search string.

# re.sub(<regex>, <repl>, <string>) finds the leftmost non-overlapping occurrences of <regex> in <string>, replaces each match as indicated by
# <repl>, and returns the result. <string> remains unchanged.
# <repl> can be either a string or a function.


# Substitution by string:
# https://realpython.com/regex-python-part-2/#substitution-by-string

# re.sub(<regex>, <repl>, <string>, count=0, flags=0)
# If <repl> is a string, then re.sub() inserts it into <string> in place of any sequences that match <regex>

# '#' replaces sequences of digits in the string:
print(re.sub(r'\d+', '#', 'foo.123.bar.789.baz'))  # foo.#.bar.#.baz

# The string '(*)' replaces sequences of lowercase letters:
print(re.sub('[a-z]+', '*', 'foo.123.bar.789.baz'))  # *.123.*.789.*

# In both cases, re.sub() returns the modified string as it always does.

# re.sub() replaces numbered backreferences (\<n>) in <repl> with the text of the corresponding captured group:
# Captured groups 1 and 2 contain 'foo' and 'quiz'.
# In the replacement string '\2,bar,baz,\1', 'foo' replaces \1 and 'quiz' replaces \2
print(re.sub(r'(\w+),bar,baz,(\w+)',  # quiz,bar,baz,foo
             r'\2,bar,baz,\1',
             'foo,bar,baz,quiz'))

# It's also possible to refer to named backreferences created with (?P<name><regex>) in the replacement string using the metacharacter sequence
# \g<name>:
print(re.sub(r'(?P<w1>\w+),bar,baz,(?P<w2>\w+)',  # quiz,bar,baz,foo
             r'\g<w2>,bar,baz,\g<w1>',
             'foo,bar,baz,quiz'))

# The backreference \g<0> refers to the text of the entire match. This is valid even when there are no grouping parentheses in <regex>:
print(re.sub(r'\d+', '/\g<0>/', 'foo 123 bar'))  # foo /123/ bar

# If <regex> specifies a zero-length match, then re.sub() will substitute <repl> into every character position in the string:
# he regex x* matches any zero-length sequence, so re.sub() inserts the replacement string at every character position in the string.
# Before the first character, between each pair of characters, and after the last character.
print(re.sub('x*', '-', 'foo123'))  # -f-o-o-1-2-3-

# If re.sub() doesn’t find any matches, then it always returns <string> unchanged.

######################################################################################

# Substitution by Function
# https://realpython.com/regex-python-part-2/#substitution-by-function

# If <repl> is a function, then re.sub() calls that function for each match found.
# It passes each corresponding match object as an argument to the function to provide information about the match.
# The function return value then becomes the replacement string.


def my_function(match_obj):

    # m.group(0) returns the entire match, and m.group() does the same.
    string = match_obj.group(0)  # The matching string

    # s.isdigit() returns True if all characters in string are digits
    if string.isdigit():
        return str(int(string) * 10)
    else:

        # Else turns all characters to upper case
        return string.upper()


print(re.sub(r'\w+', my_function, 'foo.10.bar.20.baz.30'))  # FOO.100.BAR.200.BAZ.300


# Limiting the Number of Replacements

# If a positive integer is specified for the optional count parameter, then re.sub() performs at most that many replacements.
print(re.sub(r'\w+', 'xxx', 'foo.bar.quiz.baz', count=2))  # xxx.xxx.quiz.baz

######################################################################################

# re.subn(<regex>, <repl>, <string>, count=0, flags=0)
# Returns a new string that results from performing replacements on a search string and also returns the number of substitutions made.

# e.subn() is identical to re.sub(), except that re.subn() returns a two-tuple consisting of the modified string and the number of substitutions made.
print(re.subn(r'\w+', 'xxx', 'foo.bar.quiz.baz'))  # ('xxx.xxx.quiz.baz', 4)
print(re.subn(r'\w+', my_function, 'foo.10.bar.20.baz.30'))  # ('FOO.100.BAR.200.BAZ.300', 6)

# In all other respects, re.subn() behaves just like re.sub().
