# Knowing the execution time of a program
# https://docs.python.org/3/library/time.html#time.perf_counter

# time.perf_counter() → float
# Return the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution
# to measure a short duration. It does include time elapsed during sleep and is system-wide.
# The reference point of the returned value is undefined, so that only the difference between the results of two calls
# is valid.

import time

start_time = time.perf_counter()

counter = 0
for i in range(1, 1001):
    counter += i

# perf_counter() does include time elapsed during sleep
time.sleep(3)

print(i)

end_time = time.perf_counter()
print(f'Execution time: {end_time-start_time}')
