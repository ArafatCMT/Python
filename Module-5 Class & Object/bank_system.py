# Bank System
class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.minimum_withdraw = 500
        self.maximum_withdraw = 100000

    def Get_balance(self):
        return self.balance
    
    def Deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'After deposite your balance in a account : {self.Get_balance()}')

    def Withdraw(self, amount):
        if amount < self.minimum_withdraw:
            print(f'You can not withdraw below : {self.minimum_withdraw}')

        elif amount > self.balance:
            print(f'Sorry, Not enough of money in account')

        elif amount > self.maximum_withdraw:
            print(f'You can not withdraw more than {self.maximum_withdraw} in a day')

        else:
            self.balance -= amount
            print(f'After withdraw balance of amount in your account : {self.Get_balance()}')


janata = Bank(25000)
# print(janata.Get_balance())
janata.Deposite(7500)

# janata.Withdraw(250)
janata.Withdraw(500)
janata.Withdraw(35000)
janata.Deposite(175000)
print(janata.Get_balance())
janata.Withdraw(150000)

        