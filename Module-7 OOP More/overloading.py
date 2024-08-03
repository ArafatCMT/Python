class Person: 
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Eat healty food, beacuse health is wealth")

    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.weight * other.weight
    
    def __gt__(self,other):
        return self.age > other.age

class Student(Person):
    def __init__(self, name, age, height, weight, roll):
        super().__init__(name, age, height, weight)
        self.roll = roll

    def eat(self):
        print("don\'t eat tambaco")


rahim = Student('Rahim', 21, '5.6\"', 65, 101)
karim = Student('Karim', 23, '5.6\"', 58, 102)
# print(rahim.name, rahim.age, rahim.height, rahim.weight, rahim.roll)
# rahim.eat()


print(10 + 20)
print("Sumaiya" + "Arafat")
print(karim + rahim)
print(karim * rahim)
print(karim > rahim)

