# Remove duplicate characters from a string

str = 'aaaaaBBBBcccddddddEEEEeeeffggggg'
temp = []
for i in str:
    if i not in temp:
        temp.append(i)
output = ''.join(temp)
print(output)