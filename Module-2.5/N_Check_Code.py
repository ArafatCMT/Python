num1, num2 = map(int, input().split())

str = input()

if len(str) != num1 + num2 + 1:
    print("No")
elif str[num1] != '-':
    print("No")
else:
    cnt = 0
    for c in str:
        if ord(c) >= 48 and ord(c) <= 57:
            cnt += 1
    
    if cnt == num1 + num2:
        print("Yes")
    else:
        print("No")
