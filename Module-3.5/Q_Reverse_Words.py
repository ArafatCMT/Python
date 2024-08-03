str = input()

cnt = 0

for word in str.split():
    cnt += 1

check = 1

for word in str.split():
    
    if check == cnt:
        print(word[::-1])
    else:
        print(word[::-1], end=" ")
    
    check += 1
