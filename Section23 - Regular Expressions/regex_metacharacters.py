# Regex Metacharacters
# https://realpython.com/regex-python/#python-regex-metacharacters

import re

str = 'foo123bar'
str2 = '456zihan2w'
str3 = 'asldnawe123iajsd'

# In a regex, a set of characters specified in square brackets ([]) makes up a character class.
# This metacharacter sequence matches any single character that is in the class.

# [0-9] matches any single decimal digit character—any character between '0' and '9', inclusive.
# The full expression [0-9][0-9][0-9] matches any sequence of three decimal digit characters.
match = re.search('[0-9][0-9][0-9]', str)  # Will return a match object
print(match)

match = re.search('[0-9][0-9][0-9]', str2)  # Will return a match object
print(match)

match = re.search('[0-9][0-9][0-9]', str3)  # Will return a match object
print(match)

######################################################################################
# The dot (.) metacharacter matches any character except a newline.
# 1.3 means:
# Does the string contain a '1', then any character (except a newline), then a '3'?

match = re.search('1.3', 'foo123bar')  # Will return a match object
print(match)

######################################################################################

# Metacharacters That Match a Single Character

# [ ]
# Characters inside square brackets ([]) represent a character class—an enumerated set of characters to match from.
# A character class metacharacter sequence will match any single character contained in the class.
# [123] will match any single character '1', '2' or '3'
match = re.search('ab[123]', '-----ab3---')  # Will return a match object
print(match)

match = re.search('ab[123]', '----ab1----')  # Will return a match object
print(match)

# A character class can also contain a range of characters.
# [a-z] matches any lowercase alphabetic character between 'a' and 'z', inclusive.
match = re.search('[a-z]', 'FFFabc')  # Will return a match object
print(match)

# [A-Z] matchs any uppercase alphabetic character between 'A' and 'Z', inclusive.
match = re.search('[A-Z]', 'aaaABC')  # Will return a match object
print(match)

# [0-9a-fA-F] matches any hexadecimal digit character.
match = re.search('[0-9a-fA-F]', '----MNOP--a---') # Will match the first hexadecimal digit character, 'a'.

######################################################################################

# ^ as the first character inside a character class:
# ^ as the first character matches any character that isn’t in the set.
# [^0-9] will match any character that is not a digit.
match = re.search('[^0-9]', '123456')  # Will return None, as there are only digits in the string
print(match)

######################################################################################
# Match based on whether a character is a word character

# \w and \W

# \w matches any alphanumeric word character. Word characters are uppercase and lowercase letters, digits, and the
# underscore (_) character.
# Therefore, [\w] is a shortcut for [a-zA-Z0-9_]
match = re.search('\w', '%$&=+§abc-)(}{')  # Will match the first alphanumeric character 'a'
print(match)

# [\W] matches any non-alphanumeric word character and is equivalent to [^a-zA-Z0-9_]
match = re.search('\W', '123abc')  # Will return None because there's only alphanumeric characters
print(match)

######################################################################################
# Match based on whether a character is a decimal digit

# \d and \D

# \d matches any decimal digit character.
# [\d] is the equivalent of [0-9]
match = re.search('\d', '------1---')  # Will match the digit '1'
print(match)

# \D is the opposite of \d. It matches any character that isn’t a decimal digit.
# [\D] is the equivalent of [^0-9]
match = re.search('\D', '123456789')  # Will return None as all the characters are digits
print(match)

######################################################################################
# Match based on whether a character represents whitespace

# \s and \S
# \s and \S consider a newline ('\n') to be whitespace

# \s matches any whitespace character.
match = re.search('\s', '---- ----')  # Will return a match object
print(match)

# \S matches any character that is NOT a whitespace.
match = re.search('\S', '        ')  # Will return None as all characters are whitespaces
print(match)

######################################################################################
# The character class sequences \w, \W, \d, \D, \s, and \S can appear inside a square bracket character class as well.
# [\w\s] will match any character that is alphanumeric (and _) or a whitespace
print(re.search('[\w\s]', '------123--')) # Will match the first alphanumeric character, '1'

######################################################################################

# Representing special characters
# \ Removes the special meaning of a metacharacter.
# To search for special characters that have a function, place it as the first or last character or escape it with a
# backslash (\)
match = re.search('[ab\]c]', '-----]----')  # Will match the character ']'
print(match)

# Searching for a '\' character
# Specify the <regex> using a raw string
print(re.search(r'\\', '-----\-----'))  # Will return a match with the '\' character



