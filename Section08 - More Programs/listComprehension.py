# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
myList = ['apple', 'pinaple', 'kiwi', 'banana', 'mango', 'cherry']
newList = []

# Traditional way of writing a for loop
for x in myList:
    if 'a' in x:
        newList.append(x)

print(newList)

# expression for item in list
newList = [x for x in myList if 'a' in x]
print (newList)