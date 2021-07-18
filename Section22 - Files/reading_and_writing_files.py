# Working with files in Python
# https://realpython.com/read-write-files-python/
# https://realpython.com/working-with-files-in-python/

# A file is a contiguous set of bytes used to store data.

# Files on most modern file systems are composed of three main parts:
#
# Header: metadata about the contents of the file (file name, size, type, and so on).
# Data: contents of the file as written by the creator or editor.
# End of file (EOF): special character that indicates the end of the file.

# Opening and closing a file:
# https://realpython.com/read-write-files-python/#opening-and-closing-a-file-in-python

# A file must always be closed. Either with the close() function or using the with statement.

# Writing to a file:

file = open('myfile.txt', 'w')

str = 'This is a random string\n'

# Writing something to the file
# https://realpython.com/read-write-files-python/#reading-and-writing-opened-files
file.write(str)

# Default value returned by open()
print(type(file))  # <class '_io.TextIOWrapper'>

# Closing the file
file.close()

with open('test_file.txt', 'w') as f:
    f.write(str)





