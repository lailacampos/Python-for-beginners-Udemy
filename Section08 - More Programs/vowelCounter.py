# Counting the number of vowels in a string

word = input('Enter a word: ')

# Reminder: A set does not allow duplicates. A set does not care for ordering the elements
vowels = {'a', 'e', 'i', 'o', 'u'}

results = {}  # This will create an empty dictionary. To create an empty set the function set() must be used.
for x in word:
    if x in vowels:
        # get(key) will return the value associated with the key. get(key, 'message') will return message if no such
        # key exists.
        # The first time the vowel is found in the word, the count will be 1
        # The key will be the character and the value will be the count
        results[x] = results.get(x, 0) + 1

for key, value in results.items():
    print(key, 'is present', value, 'times')
