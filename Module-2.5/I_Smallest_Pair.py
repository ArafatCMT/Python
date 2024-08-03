t = int(input())

while t != 0:
    
    n = int(input())
    
    lst = [int(ele) for ele in input().split()]

    dummy = []

    for i in range(0,n-1):

        for j in range(i+1,n):

            sum = lst[i] + lst[j] + (j - i)

            dummy.append(sum)

    print(min(dummy))

    t -= 1

