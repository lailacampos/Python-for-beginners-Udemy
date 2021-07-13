#Set type object

mySet = {10, 20, 30, 40, 'xyz'}
mySet2 = {10, 20, 30, 40, 'xyz', 10, 20}

print(mySet)
print(mySet2) #A set ignores duplicates

mySet.update([50, 60]) #Adds the objects to the end of the set
mySet.remove(60) #Removes an element from the set

#print(mySet[0]) #A set does not guarantee any order. Therefor indexing is not possible

#print(mySet * 2) is not possible as well

myFrozenSet = frozenset(mySet2) #A frozen set is read-only and does not allow for methods such as remove() and update()