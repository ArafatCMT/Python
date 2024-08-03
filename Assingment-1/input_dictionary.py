num = int(input("Enter the number of entries you went to add : "))

dic = {}

for i in range(num):
    key = input("Enter key : ")
    value = input("Enter value : ")
    dic[key] = value

print(dic)