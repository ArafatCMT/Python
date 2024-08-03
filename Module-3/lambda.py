# ak line er function toiri korte lambda use kora hoi
#function_name              parameter    return

doubled         = lambda        num   :  num * 2
total = doubled(25)
# print(total)

square = lambda num : num * num
# print(square(20))

# multiple parameter thakle

total = lambda x,y,z : x + y + z
# print(total(10,20,30))

# map()

lst = [15, 27, 39, 74, 59, 22, 56, 27, 15, 30]

doubled_lst = map(lambda num : num * 2, lst)
# print(lst)
# print(list(doubled_lst))

square_lst = map(lambda num : num ** 2, lst)
print(list(square_lst))


# filter()

actors = [
    {"name" : "safa kabir", "age" : 35},
    {"name" : "sabila noor", "age" : 30},
    {"name" : "Evana", "age" : 28},
    {"name" : "lamima", "age" : 30},
    {"name" : "tanjin tisa", "age" : 40},
    {"name" : "samira khan", "age" : 25},
    {"name" : "tasniya faria", "age" : 33}
]

# juniors = filter(lambda actor : actor["age"] < 30, actors)
# fivers = filter(lambda actor : actor["age"] % 5 == 0, actors)
# print(list(juniors))
# print(list(fivers))
