class Pen:
    # constructor
    def __init__(self, brand, ink_color, price):
        self.brand = brand
        self.ink_color = ink_color
        self.price = price


# obj_1 = Pen("Matador", "Black", 15)
# print(obj_1.brand, obj_1.ink_color, obj_1.price)

n = int(input())

lst = []

for i in range(0,n):
    brand, ink_color , price = map(str,input().split())
    price = int(price)
    obj = Pen(brand, ink_color, price)
    lst.append(obj)


for i in lst:
    print(i.brand, i.ink_color, i.price)