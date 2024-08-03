class Person:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.__balance = balance

    # getter method helps to access the private attributes from a class
    def get_balacne(self):
        return self.__balance

    # setter mehtod helps to set the value private attributes in a class
    def set_balance(self, amount):
        self.__balance += amount

    
rahim = Person("Rahim", 5000)
print(rahim.name)
print(rahim.get_balacne())
rahim.set_balance(1000)
print(rahim.get_balacne())