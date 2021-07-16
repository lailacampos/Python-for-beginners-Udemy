# Random module functions
import math
from math import *
from random import *

for i in range(5):
    number = math.floor(random()*10)
    print(number)

print()
for i in range(5):
    print(randint(1, 50))  # Return a random integer N such that a <= N <= b.

print()
for i in range(5):
    print(uniform(1,50))  # Return a random floating point number N such that a <= N <= b

print()
for i in range(5):
    print(randrange(1,50))  # Return a randomly selected element from range(start, stop, step)

print()
lst = ['Python', 'Java', 'C', 'C#', 'Javascript', 'C++', 'Html', 'CSS']
for i in range(5):
    print(choice(lst))  # Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

