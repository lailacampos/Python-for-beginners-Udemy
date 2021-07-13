#Strings and methods to manipulate them

myString = "This is a string."
myString2 = """
This is
a multi-lined
string
"""

myString3 ="   This is a string with empty spaces in the begining and the end.   "

print(myString)
print(myString2)
print(myString[0]) #Indexing - Will print the first character of the string only
print(myString*2) #Repetition - Will print the string twice
print(len(myString)) #Prints the lenght of a container. In this case, the container is the string

print(myString[0:5]) #Slicing - Prints the characters between the specified indexes
print(myString[0:]) #If the ending index is not specified, it will print until the end of the string
print(myString[:8]) #Starts from the begining and goes until the 7th character
print(myString[-7:-1]) #-1 represents the last character in a string.
print(myString[0:5:2]) #Prints beteween the specified indexes in steps of 2
print(myString[len(myString)::-1]) #Will print begining from the last character and in the reverse order
print(myString[::-1]) #Will print in the reverse order too

print(myString3.strip()) #Removes the begining and end spaces in the string
print(myString3.lstrip()) #Removes only the begining empty spaces in the string
print(myString3.rstrip()) #Removes only the end empsty spaces in the string

print(myString3.find("empty")) #Finds the sub-string inside the string and returns a number that represents the index at which the sub-string begins
print(myString3.count("a")) #Counts the number of ocurrences of a sub-string inside the string
print(myString3.replace("string", "frase")) #Replaces an string value for a new one inside the main string

print(myString.lower()) #Changed every character to lowercase
print(myString.upper()) #Changes every character to uppercase
print(myString.title()) #Changes the first character of every word to uppercase