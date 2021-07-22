# Working with time zones
# https://realpython.com/python-datetime/#working-with-time-zones

# Python datetime provides tzinfo, which is an abstract base class that allows datetime.datetime and datetime.time to
# include time zone information, including an idea of daylight saving time.
# However, datetime does not provide a direct way to interact with the IANA time zone database.
# The Python datetime.tzinfo documentation recommends using a third-party package called dateutil.

# dateutil includes an interface to the IANA time zone database.

from dateutil import tz
from datetime import datetime

# In dateutil, tz.tzlocal() returns a concrete instance of datetime.tzinfo.
now = datetime.now(tz=tz.tzlocal())
print(now)
print(now.tzname())
print()
##########################################################################################

# It's also possible to create time zones that are not the same as the time zone reported by your computer.
# To do this, you’ll use tz.gettz() and pass the official IANA name for the time zone you’re interested in.
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# Use tz.gettz() to retrieve the time zone information for London
ireland_tz = tz.gettz('Europe/Dublin')

# Retrieve the current time, setting the time zone to london_tz.
now = datetime.now(tz=ireland_tz)
print(now)
print(now.tzname())  # IST = Indian Standard Time
