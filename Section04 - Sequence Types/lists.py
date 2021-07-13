#List types

myList = [] #Empty list
myList2 = [10, -20.5, 'Laila', "Abacaxi", 54.5, 80, 'Videogame'] #Lists in python can have different types
myList3 = [10, -20.5, 48, 128, -59]

print(myList)
print(myList2[2])
print(myList2[2:5]) #Slicing
print(myList2*2) #Repetition
print(len(myList2)) #Returns the number of items in a container

myList.append(1) #Adds an element to the end of the list
myList.append(2)
myList.append(3)
myList.append(1)
print(myList)

myList.remove(1) #Removes the exact element passed as parameter once
print(myList)

myList.remove(1) #Removes 1 *AGAIN*
print(myList)

del(myList[1]) #Removes the element by index
print(myList)

myList.clear() #Removes all elements from a list
print(max(myList3)) #Returns the biggest element in the list (works not only with lists)
print(min(myList3)) #Returns the smallest element in the list (works not only with lists)

myList3.insert(3, 99) #Inserts the object at the corresponding index (the rest of the objects in the list are pushed back)
print(myList3)

myList3.sort() #Sorts numeric values in the list from smallest to largest
print(myList3)

myList3.sort(reverse=True) #Sorts numeric values in the list in the reverse order
print(myList3)

