def sum(num1, num2, num3 = 0):
    result = num1 + num2
    return result
# total = sum(10,25,5)
# print("Total is : ", total)


def all_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# total = all_sum(10,20,30,40,50)
# print(total)