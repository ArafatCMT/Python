# question : Find out which of these players is older using the operator overloading.

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __gt__(self, other):
        return self.age > other.age
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.age}"

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)
Alam = Cricketer('Alam', 40, 68, 95)

lst = [sakib, musfiq, kamal, jack, kalam, Alam]

n = len(lst)
max = sakib
# print(n)
# for i in range(0,n-1):
#     for j in range(i+1, n):
#         check = (lst[i] > lst[j])
#         if check is False :
#             # swap
#             lst[i] , lst[j] = lst[j], lst[i]
#             # print(lst[i])

# print(lst[0])

for i in range(1,n):
    if (max > lst[i]) is False:
        max = lst[i]

print(max)



