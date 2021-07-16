# Advanced Generator methods

# Use case of methods:
# .send()
# .throw()
# .close()

# A function to check if a string of number is a palindrome
# Steps:
# 1 - Capture input
# 2 - Reverse the input
# 3 - Check input vs reversed input
# 4 - If above is true: is palindrome
# 5 - If false: it's not a palindrome

# Take input
string = int(input('Enter a number: '))


def reverse(number):

    # Initiate reverse value as 0:
    reverse_number = 0

    # Check using a while loop:
    while number != 0:

        # Actual logic
        remainder = number % 10  # Rest of division. 12345 % 10 = 5

        # Multiplication by 10 adds a new place in the reversed number.
        reverse_number = reverse_number * 10 + remainder  # = 0 * 10 + 5 -> 5

        # number is then divided by 10 so that now it only contains the first 4 digits: 1234
        # // -> integer division (i.e., quotient without remainder)
        number = number // 10
    return reverse_number


reversed_number = reverse(string)
print(reversed_number)

#########################################################################
# Check if it's a palindrome


def is_palindrome(number):
    reversed_num = reverse(number)
    if number == reversed_num: return True
    else: return False


def list_palindromes():
    for i in range(1000):
        if is_palindrome(i):
            print(i)
            yield i
            if i is None:  # When next() is called, does i still have a value. ie. Is is the end of the iterable?
                yield 'End of line'


list(list_palindromes())
