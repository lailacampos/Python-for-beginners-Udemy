# Modified Regular Expression Matching With Flags
# https://realpython.com/regex-python/#modified-regular-expression-matching-with-flags

import re

# re.search(<regex>, <string>, <flags>)
# Scans a string for a regex match, applying the specified modifier <flags>.

# Flags modify regex parsing behavior, allowing for further refining of patterns.

# re.I
# re.IGNORECASE
# Makes matching case insensitive.

print(re.search('a+', 'aaaAAA'))  # match = 'aaa'
print(re.search('A+', 'aaaAAA'))  # match = 'AAA'

# Using re.I:
print(re.search('a+', 'aaaAAA', re.I))  # match = 'aaaAAA'
print(re.search('A+', 'aaaAAA', re.IGNORECASE))  # match = 'aaaAAA'

# IGNORECASE affects alphabetic matching involving character classes as well.

# When case is significant, the longest portion of 'aBcDeF' that [a-z]+ matches is just the initial 'a':
print(re.search('[a-z]+', 'aBcDeF'))  # match = 'a'

# Specifying re.I makes the search case insensitive, so [a-z]+ matches the entire string:
print(re.search('[a-z]+', 'aBcDeF', re.I))  # match = 'aBcDeF'

######################################################################################

# re.M
# re.MULTILINE
# Causes start-of-string and end-of-string anchors to match at embedded newlines.

# By default, the ^ (start-of-string) and $ (end-of-string) anchors match only at the beginning and end of the search string:
print(re.search('^foo', 'foo\nbar\nbaz'))  # match = 'foo'

# But even though the search string 'foo\nbar\nbaz' contains embedded newline characters, only 'foo' matches when anchored at the beginning of the
# string, and only 'baz' matches when anchored at the end.
print(re.search('^bar', 'foo\nbar\nbaz'))  # None
print(re.search('^baz', 'foo\nbar\nbaz'))  # None

print(re.search('baz$', 'foo\nbar\nbaz'))  # match = 'baz'

# If the MULTILINE flag is set, the ^ and $ anchor metacharacters match internal lines as well:
# ^ matches at the beginning of the string or at the beginning of any line within the string (that is, immediately following a newline).
# $ matches at the end of the string or at the end of any line within the string (immediately preceding a newline).

# Example:
print(re.search('^bar', 'foo\nbar\nbaz', re.MULTILINE))  # match = 'bar'
print(re.search('bar$', 'foo\nbar\nbaz', re.M))  # match = 'bar'

######################################################################################

# re.S
# re.DOTALL
# Causes the dot (.) metacharacter to match a newline.

# By default, the dot metacharacter matches any character except the newline character.
# The DOTALL flag lifts this restriction.

# Searches for the word 'foo' then any character (except newline), then the word 'bar'
print(re.search('foo.bar', 'foo\nbar'))  # None

print(re.search('foo.bar', 'foo\nbar', re.S))  # match = 'foo\nbar'

######################################################################################

# re.X
# re.VERBOSE
# Allows inclusion of whitespace and comments within a regex.

# The VERBOSE flag specifies a few special behaviors:
# The regex parser ignores all whitespace unless it’s within a character class or escaped with a backslash.
# If the regex contains a # character that isn’t contained within a character class or escaped with a backslash,
# then the parser ignores it and all characters to the right of it.

# It's useful because it allows for formatting a regex in Python so that it’s more readable and self-documenting.

# Example.
# The following regex does the following:

# Optional three-digit area code, in parentheses
# Optional whitespace
# Three-digit prefix
# Separator (either '-' or '.')
# Four-digit line number

regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'
print(re.search(regex, '(123) 123-4567'))  # match = '(123) 123-4567'

# Using the VERBOSE flag, it's possible to write the same regex in Python like this instead:

regex = r'''
            ^               # Anchor at the start of string
            (\(\d{3}\))?    # Optional three-digit area code, in parentheses
            \s*             # Optional whitespace
            \d{3}           # Three-digit prefix
            [-.]            # Separator character (either - or .)
            \d{4}           # Four-digit line number
            $               # Anchor at the end of string
            '''

print(re.search(regex, '(123) 123-4567', re.VERBOSE))  # match = '(123) 123-4567'

# To include a whitespace in a regex with the VERBOSE flag, escape the space character with a backslash or include it in a character class.
print(re.search('foo bar', 'foo bar', re.X))  # None
print(re.search('foo\ bar', 'foo bar'))  # match = 'foo bar'

######################################################################################

# re.DEBUG
# Displays debugging information.

# The DEBUG flag causes the regex parser in Python to display debugging information about the parsing process to the console.
# When the parser displays LITERAL nnn in the debugging output, it’s showing the ASCII code of a literal character in the regex.
print(re.search('foo.bar', 'foo-bar', re.DEBUG))  # match = 'foo-bar'
print(re.search(r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$', '123-4567', re.DEBUG))

######################################################################################

# re.A
# re.ASCII
# re.U
# re.UNICODE
# re.L
# re.LOCALE
# Specify the character encoding used for parsing of special regex character classes.

# In-depth guide about encoding in Python:
# https://realpython.com/python-encodings-guide/

# Several of the regex metacharacter sequences (\w, \W, \b, \B, \d, \D, \s, and \S) require you to assign characters to certain classes like word,
# digit, or whitespace. The flags in this group determine the encoding scheme used to assign characters to these classes.
# The possible encodings are ASCII, Unicode, or according to the current locale.

# These flags help to determine whether a character falls into a given class by specifying whether the encoding used is ASCII, Unicode,
# or the current locale

# re.U and re.UNICODE specify Unicode encoding. Unicode is the default, so these flags are superfluous.
# They’re mainly supported for backward compatibility

# re.A and re.ASCII force a determination based on ASCII encoding. If you happen to be operating in English, then this is happening anyway,
# so the flag won’t affect whether or not a match is found.

# re.L and re.LOCALE make the determination based on the current locale. Locale is an outdated concept and isn’t considered reliable.
# Except in rare circumstances, you’re not likely to need it.