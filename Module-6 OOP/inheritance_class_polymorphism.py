class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")




car = Car('Land Cruiser', 'ZX V8')
boat = Boat('Ibiza', 'Touring 20')
plane = Plane('Beoing', '747')

lst = [car, boat, plane]

for x in lst:
    print(f'{x.brand} , {x.model}')
    x.move()