# Basics of List Comprehension
# https://realpython.com/list-comprehension-python/#using-list-comprehensions

# List comprehensions are a different way of making lists.
# Instead of creating an empty list and adding each element to the end, you simply define the list and its contents
# at the same time by following this format:

# Syntax:
# new_list = [expression for item in iterable (if condition)]

# 1 - expression -> The member itself, a call to a method, or any other valid expression that returns a value.
# 2 - item -> Is the object or value in the list or iterable.
# 3 - iterable -> Is a list, set, sequence, generator, or any other object that can return its elements one at a time.
# 4 - Condition -> Optional. Only if the condition is satisfied will the item be included in the list.

# Example: Cube of numbers

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube_lst = [x ** 3 for x in lst]

print(cube_lst)

# Example 2: Even numbers in a list
# even_lst = [x for x in range(2,21,2)]
even_lst = [x for x in range(1, 21) if x % 2 == 0]
print(even_lst)
