#User will enter a number and the multiplication table for that number up until 10 will be displayed

number = int(input("Enter an integer number: "))

#Using while:
i = 1
while i <= 10:
    print(number, ' * ', i, ' = ', number * i)
    i += 1
print()

#Using for:
for x in range(1,11):
    print(x*number)