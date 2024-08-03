# break statement
num = 1

# while num <= 25:
#     print(num)
#     num += 1
#     if num == 10:
#         break

while num <= 10:
    num += 1
    if num % 2 == 1:
        continue
    print(num)