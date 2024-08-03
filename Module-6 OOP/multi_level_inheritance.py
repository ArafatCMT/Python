class Vehicle:
    def __init__(self, brand, price) -> None:
        self.brand = brand
        self.price = price

    def __repr__(self) -> str:
        return f"{self.brand} , {self.price}"
        


class Bus(Vehicle):
    def __init__(self, brand, price, seat) -> None:
        self.seat = seat
        super().__init__(brand, price)
    
    def __repr__(self) -> str:
        print(f"Bus : {self.seat}")
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, brand, price, weight):
        self.weight = weight
        super().__init__(brand, price)

    def __repr__(self) -> str:
        print("Truck")
        return super().__repr__()

class AC_Bus(Bus):
    def __init__(self, brand, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(brand, price, seat)

    def __repr__(self) -> str:
        print("Ac_Bus")
        return super().__repr__()

class PickUpTruck(Truck):
    def __init__(self, brand, price, weight):
        super().__init__(brand, price, weight)
    


green_line = AC_Bus("Green", 5000000, 25, 15)
print(green_line)        