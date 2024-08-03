str = input()

cnt = 0

flag = False

for c in str:

    if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 65 and ord(c) <= 90):
        
        if flag is False:
            cnt += 1
            flag = True
    elif (c == ' ' or c == ',' or c == '.' or c == '?' or c == '!'):
        flag = False
print(cnt)

