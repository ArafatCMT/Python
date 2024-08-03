n = int(input())
lst = [int (ele) for ele in input().split()]

mx_index = lst.index(max(lst))
mn_index = lst.index(min(lst))

lst[mx_index], lst[mn_index] = lst[mn_index] , lst[mx_index]

for x in lst:
    print(x, end=" ")
