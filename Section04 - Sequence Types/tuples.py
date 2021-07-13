#Tuples are different from lists in that they cannot be modified. They are sort o a read-only list.
'''Characteristics:
    - Can not be modified
    - Immutable
    - Maintains the insertion order when it's created
    - Allows duplicated elements
    - Allows different types of elements
'''
myTuple = (1,2,3,4,5,1,2,1) #Parentheses are optional, but it's recommended for readability
mytuple2 = 1, #If there's a single element in a tuple, there needs to be a comma after that element, otherwise it will not be treated as a tuple
myList = [2, 4, 'xyz']

print(myTuple*2) #Repetition
print(myTuple.count(1)) #Counts how many times the value occurs in the tuple
print(myTuple.index(5)) #Returns the index od the first ocurrence of the value

mytuple3 = tuple(myList) #Converts the list to a tuple
print(type(mytuple3))