# vowel_count.py

word = input('Enter a word: ').lower()
vowels = {'a', 'e', 'i', 'o', 'u'}  # type: set
results = {}  # type: dictionary

for letter in word:
    if letter in vowels:
        # get() returns the value for the specified key if key is in dictionary.
        # get() method takes maximum of two parameters:
        # key - key to be searched in the dictionary
        # value (optional) - Value to be returned if the key is not found. The default value is None.

        # letter will be the key. The value is the number of times that letter is present.
        # Initially, the letter will not be there because results is empty, so return 0.
        # Then, for the first time the vowel is found, the count will be one. (then 2, and so on)
        results[letter] = results.get(letter, 0) + 1

# Prints the each key and value in results
# items() returns a list with all the pairs key/values in a dictionary
for k,v in sorted(results.items()):
    print(k, ' is present ', v, ' times')