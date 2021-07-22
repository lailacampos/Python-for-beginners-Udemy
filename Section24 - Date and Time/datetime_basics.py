# Datetime Class
# https://realpython.com/python-datetime/

import datetime

d = datetime.date(year=2021, month=7, day=21)
t = datetime.time(hour=14, minute=35)
dt = datetime.datetime(year=2021, month=7, day=21, hour=14, minute=36, second=30)

print(d)
print(t)
print(dt)

# date.today() creates a datetime.date instance with the current local date.
print(datetime.date.today())

# datetime.now() creates a datetime.datetime instance with the current local date and time.
print(datetime.datetime.now())

# datetime.combine() combines instances of datetime.date and datetime.time into a single datetime.datetime instance.
# Creating time and date objects separately and combining them into a datetime object:

# # today -> is a date instance that has only the year, month, and day.
today = datetime.datetime.today()

# now - > is a datetime instance that has the year, month, day, hour, minute, second, and microseconds.
now = datetime.datetime.now()

# current_time -> is a time instance that has the hour, minute, and second set to the same values as now.
current_time = datetime.time(now.hour, now.minute, now.second)
print(datetime.datetime.combine(today, current_time))
