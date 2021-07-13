# remove_duplicates.py

list_with_duplicates = [10, 20, 30, 20, 50, 'apple', 20, 40, 'apple', 20]
list_without_duplicates = []

for each_value in list_with_duplicates:
    if each_value not in list_without_duplicates:
        list_without_duplicates.append(each_value)

print(list_with_duplicates)
print(list_without_duplicates)