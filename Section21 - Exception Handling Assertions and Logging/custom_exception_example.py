# Custom exception example

class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg


class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg


age = int(input('Enter your age: '))
if age < 18:
    raise TooYoungException('You are too young to drive.')
elif age > 90:
    raise TooOldException('You are too old to drive.')
else:
    print('You are eligible to drive.')


