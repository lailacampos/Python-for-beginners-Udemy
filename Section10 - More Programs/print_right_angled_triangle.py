# Print a right angled triangle

nrows = int(input('Enter the number of rows: '))
for i in range(1, nrows + 1):
    for j in range(1, i + 1):
        print('* ', end='')
    print()

# Alternatively:
print()
for i in range(1, nrows + 1):
    print('o ' * i)