from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def sleep(self):
        pass

    @abstractmethod
    def hunting(self):
        pass


class Human(Animal):
    def eat(self):
        print("I can eat")
        pass

class Tiger(Animal):
    def eat(self):
        print("I can Eat")
    
    def move(self):
        print("run very fast")

    def hunting(self):
        print("I can Hunting")


# man = Human()
# man.eat()

tiger = Tiger()
tiger.hunting()
tiger.move()