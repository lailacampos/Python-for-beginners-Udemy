# Using Strings to Create Python datetime Instances
# https://realpython.com/python-datetime/#using-strings-to-create-python-datetime-instances

from datetime import *

# date.fromisoformat(date_string)
# Return a date corresponding to a date_string given in the format YYYY-MM-DD

print(datetime.fromisoformat('2021-07-21 16:10:35'))
print(type(datetime.fromisoformat('2021-07-21')))

##########################################################################################

# To convert a string that represents a date and time but isn’t in the ISO 8601 format, use strptime()
# This method uses a special mini-language to tell Python which parts of the string are associated with the datetime
# attributes.
date_str = '09:07:35 22-07-2021'
format_str = '%H:%M:%S %d-%m-%Y'

# In format_str, there needs to be included several formatting codes and all of the dashes (-), colons (:), and spaces
# exactly as they appear in date_str.
# For every option: https://strftime.org/

# Component	                                         Code  Value

# Year (as four-digit integer )	                     %Y	   2021
# Month (as zero-padded decimal)	                 %m	   07
# Date (as zero-padded decimal)	                     %d	   22
# Hour (as zero-padded decimal with 24-hour clock)   %H    09
# Minute (as zero-padded decimal)	                 %M	   07
# Second (as zero-padded decimal)	                 %S	   35

dt = datetime.strptime(date_str, format_str)
print(dt)

