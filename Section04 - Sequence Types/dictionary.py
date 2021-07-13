#Dictionary type

dict1 = {1: 'Orange', 2:'Melon', 'Três':'Three'} #A dictionary is a pair of values: a key and a value

print(dict1)

print(dict1.items()) #Shows keys and values

k = dict1.keys() #Shows only keys
v = dict1.values() #Shows only values

for i in k: print(i)
for i in v: print(i)

print(dict1['Três']) #Prints the value of the key passed as parameter
print(dict1.get('Três'))

del dict1[2] #Removes the value associated with the parameter key

print(dict1)