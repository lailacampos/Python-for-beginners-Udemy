# Time class
# https://realpython.com/python-time-module/

# Nearly all computers count time from an instant called the Unix epoch.
# This occurred on January 1, 1970, at 00:00:00 UTC.

import time

# time.gmtime() determines the system’s epoch.
print(time.gmtime(0))

# time.time() returns the number of seconds that have passed since the epoch.
print(time.time())

# To see the current time represented as a string, pass the number of seconds you get from time() into time.ctime().
t = time.time()
print(time.ctime(t))

# If no argument is passed, then ctime() uses the return value of time() by default.
# So the following is equivalent to the above:
print(time.ctime())

##########################################################################################
# The string representation of time, also known as a timestamp, returned by ctime() is formatted with the
# following structure:

# Day of the week: Wed (Wednesday)
# Month of the year: Jul (July)
# Day of the month: 21
# Hours, minutes, and seconds using the 24-hour clock notation: 13:58:59
# Year: 2021

# The timestamp returned by ctime() depends on the geographical location.
