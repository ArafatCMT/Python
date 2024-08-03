# index :   0   1   2   3  4   5   6   7   8
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#index  :  -9  -8  -7  -6  -5  -4  -3  -2  -1


# print(numbers[4], numbers[-8])

#list ( start : end ) start from start index and stop before the end index
# print(numbers[3:7])
# print(numbers[-8:-2])

#list ( start : end : step)
# print(numbers[1:7:2])
# print(numbers[7:1:-2])
# print(numbers[4:])
# print(numbers[:7])
# print(numbers[::-1]) #shortcut to reverse a list
# print(numbers[:]) #shortcut to copy a list

# input list
lst = []
n = int(input())

for i in range(0,n):
    ele = int(input())
    lst.append(ele)

print(lst)



