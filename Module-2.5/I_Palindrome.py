n = int(input())
lst = []

while n != 0:
    rem = n % 10
    lst.append(rem)
    n = n // 10

i = 0
j = len(lst) - 1
flag = True

while i < j:
    if lst[i] != lst[j]:
        flag = False
        break
    i += 1
    j -= 1

while len(lst) != 0:
    if lst[0] == 0:
        lst.remove(0)
    if(lst[0] != 0):
        break

sum = 0

for i in lst:
    sum = (sum * 10) + i
    
print (sum)

if flag is True:
    print("YES")
else:
    print("NO")