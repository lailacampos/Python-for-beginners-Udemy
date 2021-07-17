# Product of two lists

lst1 = list(range(1,11))
lst2 = [1, 3, 27, 50, 6, 14, 22, 100, 3, 2]
product_lst = []
print(lst1)
print(lst2)

# for i in range(len(lst1)):
#     common_elements_lst.append(lst1[i] * lst2[i])

product_lst = [lst1[i] * lst2[i] for i in range(len(lst1))]

print(product_lst)
