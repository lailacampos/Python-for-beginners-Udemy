# The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be
# executed.
myList = eval(input('Enter a list of elements: '))
print(myList)

nonDuplicateList = []

for each_value in myList:
    # not in -> Returns True if a sequence with the specified value is not present in the object
    if each_value not in nonDuplicateList:
        nonDuplicateList.append(each_value)
print(nonDuplicateList)

# With set:

# A set does not allow duplicates
set1 = set(myList)

# Reminder: order does not matter in a set object
print(set1)
print(type(set1))
