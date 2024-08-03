n = int(input())

cnt = 0

lst = [int(ele) for ele in input().split()]

# even count 
for i in lst:
    if i % 2 == 0:
        cnt += 1

op = 0

if cnt == n:

    flag = True

    while True:

        for i,num in enumerate(lst):

            if num % 2 == 0 and num != 0:

                lst[i] = lst[i] // 2
            
            else:

                flag = False
                break
        
        if flag is False:
            break
            
        op += 1
    
    print(op)

else:
    print(0)


