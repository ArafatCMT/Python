n , q = map(int, input().split())

lst = [int (ele) for ele in input().split()]

pre_lst = []

pre_lst.append(lst[0])

for i, val in enumerate(lst):

    if i >= 1:
        sum = lst[i] + pre_lst[i-1]
        pre_lst.append(sum)

while q != 0:
    
    left, right = map(int, input().split())

    left -= 1
    right -= 1

    if left == 0:
        print(pre_lst[right])
    else:
        print(pre_lst[right] - pre_lst[left-1])
    
    q -= 1