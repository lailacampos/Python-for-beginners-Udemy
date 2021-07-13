minNumber = int(input("Enter minimum number: "))
maxNumber = int(input("Enter maximum number: "))

i = minNumber

if minNumber % 2 == 0: i = minNumber + 1
while i <= maxNumber:
    print(i)
    i+=2