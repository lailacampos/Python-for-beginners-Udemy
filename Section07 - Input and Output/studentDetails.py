studentId = int(input("Enter student id: "))
name = input("Enter student name: ")
#grades = float(input("Enter student grades: ").split(','))

grades = [x for x in input("Enter student grades: ").split(',')]
gradesFloat = []
for x in grades: #Will transform every object in the list into float objects
    gradesFloat.append(float(x)) #Append -> Inserts object to the end of the list

print("Id: ", studentId)
print("Name: ", name)
print(gradesFloat)
print(type(gradesFloat[0]))