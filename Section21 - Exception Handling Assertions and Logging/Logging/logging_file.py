# Logging to a file

import logging

# For logging to a file rather than the console, filename and filemode parameters can be used.

# About handling files in Python: https://www.geeksforgeeks.org/reading-writing-text-files-python/
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s', level=logging.DEBUG)

logging.debug('Debug')  # DEBUG:root:Debug
logging.info('Info')  # INFO:root:Info
logging.warning('Warning')  # WARNING:root:Warning
logging.error('Error')  # ERROR:root:Error
logging.critical('Critical error')  # CRITICAL:root:Critical error
