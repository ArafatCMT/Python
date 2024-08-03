"""
Difference between Class method and Static method  :

Class method : 

1. A class method takes cls as the first parameter.
2. A class method can access or modify the class state.
3. Class must be a parameter for class method.
4. It uses @classmethod decorator.

Static method : 

1. Static method needs no specific parameters.
2. Static method cannot access or modify the class state.
3. Static methods are typically unaware of the class state. They are utility methods that operator on some parameters after receiving them.
4. It uses @staticmethod decorator.

"""

# example : 

class Person:
    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age
        pass

    @classmethod
    def my_data(cls, name,age):
        # return f"{name} {age}"
        return cls(name,age)
    
    @staticmethod
    def isAdult(age):
        if age > 18:
            return f"Yes"
        else:
            return f"No"
        
# obj = Person("manik")
# manik = obj.my_data('manik',16)
# print(manik)
a = Person.my_data("manik",10)
print(a.age)
# print(Person.my_data("manik", 10))
# print(Person.isAdult(19))