#Reverse the characters in each word

# Input  -> This is a sample string
# Output -> sihT si a elpmas gnirts

str = 'This is a sample string'
temp_str = str.split()
print(temp_str)
result = []
i = 0

while i < len(temp_str):
    result.append(temp_str[i][::-1])
    i+=1

output = ' '.join(result)
print(output)
