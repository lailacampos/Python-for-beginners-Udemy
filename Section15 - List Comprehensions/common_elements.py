# Commmon elements of two lists

lst1 = list(range(1,21))
lst2 = [1, 3, 27, 50, 6, 14, 22, 100, 3, 2, 33, 2, 17]
common_elements_lst = []

# for i in lst1:
#     if i in lst2:
#         common_elements_lst.append(i)

common_elements_lst = [i for i in lst1 if i in lst2]
print(common_elements_lst)
