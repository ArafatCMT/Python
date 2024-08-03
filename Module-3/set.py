lst = [15, 27, 39, 74, 59, 22, 56, 27, 15, 30]

lst_set = set(lst) # lst convert to set
print(lst)
print(lst_set)

lst_set.add(55)
lst_set.add(55)
lst_set.add(55)
print(lst_set)
lst_set.remove(39)
print(lst_set)

# lst_set[2] = 54
print(lst_set)

A = {1,2,3,4,5,7}
B = {2,4,6,7,8,9}

print(A & B)
print(A | B)

