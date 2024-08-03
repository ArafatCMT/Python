n = int(input())

str = input()

sum = 0

for char in str:
    
    ascii_value = ord(char)
    sum += ascii_value - 48

print(sum)