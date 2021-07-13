# Print a pyramid

nrows = int(input('Enter the number of rows: '))
#   *    -> (number of rows) - 1 = empty spaces
#  * *   -> (number of rows) - 2 = empty spaces
# * * *  -> and so on

for i in range(1, nrows + 1):
    print(' ' * (nrows - i), end='')
    print('* ' * i)
