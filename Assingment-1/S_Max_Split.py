str = input()

l = 0
r = 0
lst = []
str_2 = ""

for i in str:
    
    if i == 'L':
        l += 1
        str_2 += 'L'
    else:
        r += 1
        str_2 += 'R'
    
    if (l == r):
        lst.append(str_2)
        str_2 = ""
        l = 0
        r = 0

print(len(lst))

for i in lst:
    print(i)


