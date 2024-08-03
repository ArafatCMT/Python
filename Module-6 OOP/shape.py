from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am two-dimentional shape."
    

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius
    

rectangle = Rectangle('Rectangle', 20, 25)
circle = Circle('Circle', 12)

print(rectangle.name)
print(rectangle.area())
print(rectangle.fact())

print(circle.name)
print(circle.fact())
print(circle.area())