# Even or odd

# lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>
l = lambda x: 'Yes' if x%2==0 else 'No'  # Yes if number is even, No if number is odd
print(l(10))
print(l(9))
