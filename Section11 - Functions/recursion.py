# Recursion
# The process of a function calling itself
# Each time a recursive call is made, a smaller problem is solved,
# until it gets to a point where the problem cannot get any smaller.
#
# A good time to use recursion is when the same logic is repeating

# A function that calls itself recursively must have a plan to eventually stop.
# Recursive functions typically follow this pattern:#
# There are one or more base cases that are directly solvable without the need for further recursion.
# Each recursive call moves the solution progressively closer to a base case.

########################################################

# Example 1

def factorial(num):
    # The very first step to start a recursion function is to define an end condition: a way to escape.
    # Else, it will go on an infinite loop
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# Step by step walkthrough:
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 * factorial(0)
# factorial(0) = 1
#
# factorial(3) = 3 * 2 * 1 * 1
# factorial(3) = 6

print('factorial(3): ', factorial(3))


########################################################
# Example 2

# Calculate the sum of a list of numbers
def sum_function(lst):
    # If there's only one element in the list, return that element
    if len(lst) == 1:
        return lst[0]
    else:
        # Else, return the first element plus the next element in the list
        return lst[0] + sum_function(lst[1:])


# sum_function([1, 2, 3]) = 1 + sum_function([2, 3])
# sum_function([2, 3]) = 2 + sum_function([3])
# sum_function([3]) = 3
#
# sum_function([1, 2, 3]) = 1 + sum_function([2, 3])
# sum_function([2, 3]) = 2 + 3
#
# sum_function([1, 2, 3]) = 1 + 5
#
# sum_function([1, 2, 3]) = 6

print('sum_function([1, 2, 3]): ', sum_function([1, 2, 3]))


########################################################
# Example 3

# Calculate the sum of the numbers in a non negative integer
def sum_digits(num):
    if num == 0:
        return 0
    else:
        # Return the rest part of a division by 10, plus that number divided by 10
        return num % 10 + sum_digits(int(num / 10))

# sum_digits(123) -> 123 % 10 = 3, + (sends 123/10 to the next step)
# sum_digits(12) -> 12 % 10 = 2, + (sends 12/10 to the next step)
# sum_digits(1) -> 1 % 10 = 1 + (sends 1/10 to the next step)
# sum_digits(0) -> 0, algorithm stops

# sum_digits(123) -> 3 + 2 + 1 = 6

print('sum_digits(123): ', sum_digits(123))

########################################################
# Example 4

# Calculate the value of 'a' to the power 'b'
def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b -1)

# power(2, 3) -> 2 * power(2, 2)
# power(2, 2) -> 2 * power(2, 1)
# power(2, 1) -> 2 * power(2, 0)
# power(2, 0) -> 2 * 1
#
# power(2, 3) -> 2 * power(2, 2)
# power(2, 2) -> 2 * power(2, 1)
# power(2, 1) -> 2
#
# power(2, 3) -> 2 power(2, 2)
# power(2, 2) -> 2 * 2
#
# power(2, 3) -> 2 * 4
#
# power(2, 3) = 8

print('power(2,3): ', power(2, 3))