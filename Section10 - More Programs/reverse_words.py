#Reverse words in a string

str = 'This is a random string'
# split() splits a string into a list.

# string.split(separator, maxsplit)

# Separator	is optional. It specifies the separator to use when splitting the string.
# By default any whitespace is a separator

# Maxsplit is optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

temp = str.split()
print(temp)
result = []
i = len(temp) - 1
while i >= 0:
    result.append(temp[i])
    i = i -1

output = ' '.join(result)
print(output)