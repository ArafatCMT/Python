str = input()
 
L_cnt = 0
lst = []
str_lst = []
 
for i,char in enumerate(str):

    if char == 'L':
        L_cnt += 1
        if str[i+1] == 'R':
            lst.append(L_cnt*2)

    else:
        L_cnt -= 1

for i in lst:
    ans = ""
    for j in range(1,i+1):
        mid = i // 2
        if j <= mid:
            ans += 'L'
        else:
            ans += 'R'
    # print(ans)
    str_lst.append(ans)

print(len(str_lst))

for i in str_lst:
    print(i)