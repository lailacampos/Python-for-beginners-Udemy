# Break and continue

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in myList:
    if i == 7:
        break #Breaks out of the loop statement, not of the if condition
    print(i)

x = 0
while x < 20:
    x += 1
    if x % 3 == 0:
        continue #Skips the current iteration in a loop and continues to the next
    print(x)