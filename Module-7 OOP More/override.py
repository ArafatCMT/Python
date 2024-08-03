class Person: 
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Eat healty food, beacuse health is wealth")
    
    def move(self):
        raise NotImplementedError

class Student(Person):
    def __init__(self, name, age, height, weight, roll):
        super().__init__(name, age, height, weight)
        self.roll = roll

    def eat(self):
        print("don\'t eat tambaco")

    def move(self):
        print("move fast")


rahim = Student('Rahim', 21, '5.6\"', 65, 101)
# print(rahim.name, rahim.age, rahim.height, rahim.weight, rahim.roll)
rahim.eat()
rahim.move()