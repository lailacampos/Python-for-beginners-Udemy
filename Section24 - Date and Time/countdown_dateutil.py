# Countdown using Dateutil

from dateutil import parser, tz
from datetime import datetime

# A countdown that takes time zones into consideration

# parse offers a generic date/time string parser which is able to parse most known formats to represent a date
# and/or time

# Use parser.parse() to read the date of the beginning of vacation from a string.
VACATION_DATE = parser.parse('December 15, 2021 10 PM')

# parser.parse() returns a naive datetime instance, so use .replace() to change the tzinfo to the America/Fortaleza
# time zone.
# PYCON_DATE is an aware datetime instance
VACATION_DATE = VACATION_DATE.replace(tzinfo=tz.gettz('America/Fortaleza'))
now = datetime.now(tz=tz.tzlocal())

countdown = VACATION_DATE - now
print(countdown)

# About aware and naive datetime instances:
# https://realpython.com/python-datetime/#comparing-naive-and-aware-python-datetime-instances
