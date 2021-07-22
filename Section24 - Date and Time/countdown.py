# Creating a countdown

from datetime import datetime

BIRTHDAY_DATE = datetime(year=2021, month=10, day=24)
countdown = BIRTHDAY_DATE - datetime.now()
print(f"Countdown to Laila's birthday: {countdown}")

# The difference between two datetime instances returns a datetime.timedelta instance.
# timedelta instances represent the change in time between two datetime instances.
