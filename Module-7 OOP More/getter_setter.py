# getter --> get the value of a proporty through a method.most of the, time you will get the value of a private attribute
# setter --> set the value of a property through a method . most of the , time you will set the value of a private attribute
# read only --> you can not change the value
class User:
    def __init__(self, name, age, money):
        self._name = name 
        self._age = age
        self.__money = money
    
    # getter without any setter is read only attribute
    @property
    def get_money(self):
        return self.__money
    
    @get_money.setter
    def increarse_money(self, money):
        if money > 0:
            self.__money += money
        else:
            print("negative value not possible")


rahim = User('Rahim', 21, 500)
# print(rahim.get_money())
print(rahim.get_money)

# rahim.increarse_money(500)
rahim.increarse_money = 1000
print(rahim.get_money)

        