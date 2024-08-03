# class Family:
#     def __init__(self, Address):
#         self.Address = Address

# class School:
#     def __init__(self, name, roll, cls) -> None:
#         self.name = name
#         self.roll = roll
#         self.cls = cls

# class Sports:
#     def __init__(self, club, game) -> None:
#         self.club = club
#         self.game = game


# class Student(Family, School, Sports):
#     def __init__(self, name, roll, cls, club, game, Address):
#         Family.__init__(self, Address)
#         School.__init__(self, name, roll, cls)
#         Sports.__init__(self, club, game)



class Student:
    def __init__(self, name, roll) -> None:
        self.name = name 
        self.roll = roll



class Player:
    def __init__(self, jersey_number, club) -> None:
        self.jersey_number = jersey_number
        self.club = club



class Singer:
    def __init__(self, brand) -> None:
        self.brand = brand




class Person(Student, Player, Singer):
    def __init__(self, name, roll, jersey_number, club, brand) -> None:
        Student.__init__(self, name, roll)
        Player.__init__(self, jersey_number, club)
        Singer.__init__(self, brand)
        # super().__init__(name, roll)

person = Person('Arafat', 102, 10, 'jomuna', "Sheronamhin")
print(person.name, person.roll, person.jersey_number, person.club, person.brand)