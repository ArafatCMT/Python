# static attribute (class attribute)
# static method decorate by @staticmethod
# class method decorate by @classmethod
# difference between static method and class method

class Shopping:
    car = [] # class attribute / static attribute
    def __init__(self, name) -> None:
        self.name = name
    
    @classmethod
    def display(self, name):
        print(f"welcome to our shoppingmol :{name}")

    @staticmethod
    def addition(num1, num2):
        print(num1 + num2)


AR_corner = Shopping("AR Corner")
AR_corner.display('ar_mlaza')
# Shopping.display('AR_Corner')

Shopping.addition(10,20)
        