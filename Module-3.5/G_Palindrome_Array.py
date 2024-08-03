n = int(input())

lst = [int(ele) for ele in input().split()]

i = 0
j = len(lst) - 1

flag = True

while i < j:

    if lst[i] != lst[j]:
        flag = False
        break
    
    i += 1
    j -= 1

if flag is True:
    print("YES")
else:
    print("NO")