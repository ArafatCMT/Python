""" 
Operator overloading : operator overloading means giving extended meaning beyond their predefined operational meaning.
For example operator ‘+’ is used to add two integers as well as join two string and merge two list.
It because ‘+’ operator is overloaded by int class and str class.

"""
# Example :

class Something:
    def __init__(self, value) -> None:
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
    

obj_1 = Something(10)
obj_2 = Something(20)

# adding two intger number
print(obj_1 + obj_2)


obj_3 = Something("Ressul")
obj_4 = Something("Jacson")

# concatenate two string
print(obj_3 + obj_4)