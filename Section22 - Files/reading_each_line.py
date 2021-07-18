# Iterating Over Each Line in the File
# https://realpython.com/read-write-files-python/#iterating-over-each-line-in-the-file

# Read methods that can be called on a file object:

# .read(size=-1) -> This reads from the file based on the number of size bytes. If no argument is passed or None or -1
# is passed, then the entire file is read.

# .readline(size=-1) -> This reads at most size number of characters from the line.
# This continues to the end of the line and then wraps back around.
# If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.

# .readlines()	This reads the remaining lines from the file object and returns them as a list.
# readlines() returns a list where each element in the list represents a line in the file

# Using readline()
with open('dog_breeds.txt', 'r') as file:
    line = file.readline()
    while line != '':  # The EOF (end of file) is an empty string

        #  end='' is to prevent Python from adding an additional newline to the text that is being printed and
        #  only print what is being read from the file.
        print(line, end='')
        line = file.readline()

print()
print()
# Using readlines()
with open('dog_breeds.txt', 'r') as file2:
   for line in file2.readlines():
       print(line, end='')

print()
print()

# Iterating each line of the file itself
with open('dog_breeds.txt', 'r') as file3:
    for line in file3:
        print(line, end='')
