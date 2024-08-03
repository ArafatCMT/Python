n = int(input())

lst = [int(ele) for ele in input().split()]

cnt_lst = []

for i in range(n+1):
    cnt_lst.append(0)

for i in lst:
    if i <= n:
        cnt_lst[i] += 1

cnt = 0

for i in range(1,n+1):

    if cnt_lst[i] >= i:
        cnt += i

print(n - cnt)