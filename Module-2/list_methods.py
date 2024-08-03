numbers = [{20, 45, 14, 60, 48, 50, 62, 27, 33}]

numbers.append(100)
numbers.append(50)
numbers.append(50)
numbers.append(50)
numbers.append(50)
# print(numbers)

numbers.insert(5,80)
print(numbers)

if 60 in numbers:
    numbers.remove(60)
    print(numbers)

if 95 in numbers:
    numbers.remove(95)
    print(numbers)

last = numbers.pop()
print(last, numbers)

x = numbers.pop(2)
print(x, numbers)

if 62 in numbers:
    index = numbers.index(62)
    print(index)

if 60 in numbers:
    index = numbers.index(60)
    print(index)

count = numbers.count(50) 
print(count)

numbers.sort()
print(numbers)


# numbers.reverse()
# print(numbers)


