# Arithmetics with datetime
# https://realpython.com/python-datetime/#doing-arithmetic-with-python-datetime

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now()
print('Today: ', now)
tomorrow = timedelta(days=+1 )
print('Tomorrow: ', now + tomorrow)

# timedelta instances also support negative values as the input to the arguments
yesterday = timedelta(days=-1)
print('Yesterday: ', now + yesterday)

# timedelta instances support addition and subtraction as well as positive and negative integers for all arguments.
delta = timedelta(days=+3, hours=-4)

# Three days in the future minus 4 hours:
print('Plus 3 days, minus 4 hours from now: ', now + delta)

##########################################################################################

# timedelta() is somewhat limited because it cannot add or subtract intervals larger than a day, such as a month or a
# year.
# For that case, dateutil provides a more powerful replacement called relativedelta.

delta = relativedelta(years=+2, months=+4, days=+23, hours=-4, minute=+30)
print("2 years, 4 months, 23 days, -4 hours and 30 minutes into the future: ", now + delta)


