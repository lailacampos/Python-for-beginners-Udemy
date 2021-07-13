# Count characters in a string

str = 'aaaaBBBBbbbbcccdEEEEEEEfffGGadushgeasbdaushdasd'
temp = {}

for i in str:
    temp[i] = temp.get(i, 0) +1

for k, v in temp.items():
    print('{} = {} times'.format(k,v))

# Alternatively:
temp = {}
for i in str:
    if i in temp:
        temp[i] = temp[i] + 1  # temp[i] += 1
    else:
        temp[i] = 1

print(temp)
