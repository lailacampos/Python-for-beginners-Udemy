# reverse_string.py

# String indexing relevant link:
# https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

# 1st way: Using indexing
s = input('Enter a string: ')
print('Using indexing:   ', s[::-1])

# 2nd way: Using for loop and appending characters in reverse order
# indexing starts from 0
reverse_string = ''  # Declaring empty string to store the reversed string
for i in s:
    # Starts with the first letter in the string.
    # Then concatenates the next letter with the first letter, in this order, and so on.
    # The result is a reversed string.
    # The result is a reversed string.
    reverse_string = i + reverse_string

print('Using for loop:   ', reverse_string)

# 3 - Using while loop
reverse_string = ''
count = len(s)  # Find length of a string and save in count variable
while count > 0:
    # Concatenates letter by letter, starting from the last letter.
    reverse_string = reverse_string + s[count -1]
    count = count -1
print('Using while loop: ', reverse_string)

# 4 - Using join()
reverse_string = ''.join(reversed(s))
print('Using join():     ', reverse_string)

# 5 - Using recursion
def reverse(str):
    if len(str) == 0:  # Checking for the length of the string
        return str
    else:
        return reverse(str[1:]) + str[0]  # Obs: study recursion later

print('Using recursion:  ', reverse(s))