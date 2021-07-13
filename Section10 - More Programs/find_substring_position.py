# Find substring position inside a given string

str = 'Take up one idea and make that idea your life. Think and dream of that idea and leave every other idea alone'
substr = 'idea'
found = False
position = -1
length = len(str)

while True:
    position = str.find(substr, position + 1, length)
    if position == -1:  # substring not found
        break
    print('Found substring at position ', position)
    found = True

if found == False:
    print("Substring not found")