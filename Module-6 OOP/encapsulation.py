# encapsulation --> hide details
# Access Modifires --> public, private, protect

class Bank:
    def __init__(self, holder_name, balance) -> None:
        self.holder_name = holder_name # public
        self._branch = 'Bonani 11' # protect
        self.__balance = balance # private

    def get_balance(self):
        return self.__balance
    
    def deposite(self, amount):
        if 0 < amount:
            self.__balance += amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
        


jonota = Bank('Arafat', 2500)
# print(jonota.holder_name)
# # jonota.balance = 0
# # print(jonota.get_balance())   
# jonota.deposite(500)
# print(jonota.get_balance())
# jonota.holder_name = 'Afridi'
# print(jonota.holder_name)

# print(jonota._branch)
# jonota.withdraw(1000)
# print(jonota.get_balance())

print(jonota.__balance)