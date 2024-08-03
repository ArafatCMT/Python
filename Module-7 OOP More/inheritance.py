# inheritance provides "is a" relation

class Animal:
    def __init__(self) -> None:
        pass

# cat is a animal
class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

# dog is a animal
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()


class Furniture:
    def __init__(self) -> None:
        pass

# chair is a furniture
class Chair(Furniture):
    def __init__(self) -> None:
        super().__init__()