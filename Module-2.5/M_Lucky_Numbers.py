num1, num2 = map(int, input().split())

lst = []

for num in range(num1,num2+1):

    flag = True
    number = num

    while num != 0:

        rem = num % 10

        if rem != 4 and rem != 7:
            flag = False
            break
        
        num = num // 10
    
    if flag is True:
        lst.append(number)

if len(lst) == 0:
    print("-1")
else:
    for x in lst:
        print(x, end=" ")
