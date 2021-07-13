#Range type

myRange = range(5) #How to define a range object. It will create a range with the parameter as the last value and starting from 0
myRange2 = range(1,6) #A range that begins with 1 and ands with 5 (it excludes the last value)
myRange3 = range(1,15,2) #The third parameter represents the step -> How many numbers it should skip when counting

#For each object i in myRange
for i in myRange3:
    print(i)
