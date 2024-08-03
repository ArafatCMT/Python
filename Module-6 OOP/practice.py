from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

    def fact(self):
        return f'I am two-dimentional shape.'
    

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius
    

rect = Rectangle('Rectangle', 15, 25)
cir = Circle('Circle', 12)

print(cir.name)
print(cir.area())
print(cir.fact())