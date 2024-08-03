class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car = Car('Land Cruiser', 'ZX V8')
boat = Boat('Ibiza', 'Touring 20')
plane = Plane('Beoing', '747')

vehicle = [car, boat, plane]
for x in vehicle:
    x.move()
        