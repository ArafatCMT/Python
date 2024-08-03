n = int(input())
lst = [int(x) for x in input().split()]
lst.sort()
print(lst)

# double = map(lambda val : val % 2 == 0, lst)
double = filter(lambda val : val % 2 == 0, lst)
print(list(double))
