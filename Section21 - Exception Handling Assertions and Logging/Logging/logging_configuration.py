# Logging configuring
# https://realpython.com/python-logging/#basic-configurations

import logging

# By default, the logging module logs the messages with a severity level of WARNING or above.
# By using the level parameter in logging.basicConfig the root logger will be set to the specified severity level.
# logging.basicConfig can only be called once.

# The default setting in basicConfig() is to set the logger to write to the console in the following format:
# ERROR:root:Error message

# The recommended way of string formatting is to pass the actual message with string formatting specifiers
# (%s, %r, %x etc.)

# https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Debug')  # DEBUG:root:Debug
logging.info('Info')  # INFO:root:Info
logging.warning('Warning')  # WARNING:root:Warning
logging.error('Error')  # ERROR:root:Error
logging.critical('Critical error')  # CRITICAL:root:Critical error
