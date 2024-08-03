# method overriding :  whenever we writing method name with same signature in parent and child class , than we called him method overloading.
# Example : 

class Parent:
    def display(self):
        print("I am the parent class")

class Child(Parent):
    def display(self):
        print("I am the child class")

child = Child()
child.display()

