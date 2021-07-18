# Logging and exceptions

# If logging from an exception handler, use the logging.exception() method, which logs a message with level ERROR and
# adds exception information to the message.
# To put it more simply, calling logging.exception() is like calling logging.error(exc_info=True).
# But since this method always dumps exception information, it should only be called from an exception handler.

import logging

logging.basicConfig(filename='app.log', filemode='w')

a = 10
b = 0

try:
    c = a/b
except Exception as e:
    logging.exception('Exception occurred')