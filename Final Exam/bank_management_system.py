from datetime import datetime

class Bank:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.__available_balance = 0 # total balance store in bank
        self.__total_loan = 0   # total loan in bank
        self.__is_loan_active = True
    
    def get_available_balance(self):
        return self.__available_balance

    def set_available_balance(self, amount, option):
        # option 1 means deposite 
        # option 0 means withdraw
        if option == 1:
            self.__available_balance += amount
        else:
            self.__available_balance -= amount
    
    def get_total_loan(self):
        return self.__total_loan
    
    def set_total_loan(self, amount):
        self.__total_loan += amount
    
    def add_user(self, user):
        self.users[user.account_number] = user

    def show_users(self):
        print("\n\tUsers:\n")
        print("\tName\t\tAddress\t\tAccount_Type\tAccount_Number")
        for key,user in self.users.items():
            print(f"\t{user.name}\t\t{user.address}\t\t{user.account_type}\t\t{key}")
    
    def remove_user(self, account_number):
        if account_number in self.users:
            balance = self.users[account_number].get_balance()
            self.set_available_balance(balance, 0)

            del self.users[account_number]
            print("\n\tAccount Delete Successfully!!")
        else:
            print("\n\tAccount does not exist!!")

    def find_account(self, account_number):
        if account_number in self.users:
            return self.users[account_number]
        else:
            return None
        
    def get_loan_active_status(self):
        return self.__is_loan_active
    
    def set_loan_active_status(self, option):
        if option == 'on':
            self.__is_loan_active = True
            print("\n\tBank Loan Active Status is ON!!")
        elif option == 'off':
            self.__is_loan_active = False
            print("\n\tBank Loan Active Status is OFF!!")
        else:
            print("\n\tInvalid Option!!")

class Transacton:
    def __init__(self, amount, date, account_number):
        self.amount = amount
        self.date = date
        self.account_number = account_number

class User:
    def __init__(self, name, email, address, account_type, password):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.account_number = name + email
        self.loan = 2
        self.__balance = 0
        self.deposit_history = [] # database : deposite history
        self.withdraw_history = [] # database : withdraw history
        self.transfer_history = [] # database : transfer history
        self.receive_amount_history = [] # database : amount received history

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount, bank):
        if amount > 0:
            self.__balance += amount
            print("\n\tDeposite Successfully!!")
            deposit = Transacton(amount, datetime.now(), self.account_number)
            self.deposit_history.append(deposit)
            bank.set_available_balance(amount, 1)
        else:
            print("\n\tAmount less then 0")
    
    def withdraw(self, amount, bank):
        if self.__balance == 0:
            print("\n\tBank is Bankrupt!!")

        elif amount <= self.__balance:
            self.__balance -= amount
            withdraw = Transacton(amount, datetime.now(), self.account_number)
            self.withdraw_history.append(withdraw)
            bank.set_available_balance(amount, 0)
            print("\n\tWithdraw Successfully!!")

        else:
            print("\n\tWithdrawal amount exceeded!!")

    def transactions(self, option):
        print("\nTransactions:\n")
        if option == 1:
            print("\n\tDeposite:\n")
            print("\tAmount\tDate\t   Time")
            for obj in self.deposit_history:
                print(f"\t{obj.amount}\t{obj.date}")

        elif option == 2:
            print("\n\tWithdraw History:\n")
            print("\tAmount\tDate\t   Time")
            for obj in self.withdraw_history:
                print(f"\t{obj.amount}\t{obj.date}")

        elif option == 3:
            print("\n\tTransfer Amount History:\n")
            print("\tAmount\tAccount_Number\t\tDate")
            for obj in self.transfer_history:
                print(f"\t{obj.amount}\t{obj.account_number}\t{obj.date}")

        elif option == 4:
            print("\n\tReceived Amount History:\n")
            print("\tAmount\tAccount_Number\t\tDate")
            for obj in self.receive_amount_history:
                print(f"\t{obj.amount}\t{obj.account_number}\t{obj.date}")

        else:
            print("\n\tInvalid Input!!")

    
    def take_loan(self, amount, bank):
        if bank.get_loan_active_status() is False:
            print("\n\tLoan Feature of Bank is OFF!!")

        elif self.loan <= 0:
            print("\n\tSorry ! Already take loan two times")

        else:
            self.__balance += amount
            self.loan -= 1
            bank.set_total_loan(amount)
            bank.set_available_balance(amount, 1)
            print("\n\tLoan Take Successfully!!")
    
    def transfer_amount(self, amount,account_number, bank):
        user = bank.find_account(account_number)
        if user:
            if amount <= self.__balance:
                self.__balance -= amount
                user.__balance +=  amount
                print("\n\tAmount Transfer successfully!!")
                transfer = Transacton(amount, datetime.now(), account_number)
                receive = Transacton(amount, datetime.now(), self.account_number)
                self.transfer_history.append(transfer)
                user.receive_amount_history.append(receive)
            else:
                print("\n\tTransfer Amount Exceeded!!")
        else:
            print("\n\tAccount does not exist!!")

class Admin:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def create_account(self, name, email, address, account_type, password, bank):
        newAccount = User( name, email, address, account_type, password)
        bank.add_user(newAccount)
        print("\n\tAccount Create Successfully!!")

    def show_users(self, bank):
        bank.show_users()
    
    def remove_account(self, account_number, bank):
        bank.remove_user(account_number)
    
    def check_available_balance(self, bank):
        print(f"\n\tAvailable Balance: {bank.get_available_balance()}")
    
    def check_loan_balance(self, bank):
        print(f"\n\tTotal Loan Balance: {bank.get_total_loan()}")
    
    def on_off_loan_feature(self, option, bank):
        bank.set_loan_active_status(option)

bank = Bank("Gorib er Bank")
admin = Admin("Admin", 1234)

# customer interface
def user_interface(user):

    while True:
        print("\n\t-----------------")
        print("\t  **Welcome**")
        print("\t-----------------\n")
        print("1. Deposit")
        print("2. Withdraw")           
        print("3. View Available Balance")
        print("4. Take Loan")
        print("5. View Transaction")
        print("6. Amount Transfer Another Account")
        print("7. Exit\n")

        option = int(input("Enter Option: "))

        if option == 1:
            amount = int(input("\tEnter Amount: "))
            user.deposit(amount, bank)
        
        elif option == 2:
            amount = int(input("\tEnter Amount: "))
            user.withdraw(amount, bank)
        
        elif option == 3:
            print(f"\n\tAvailable Balance : {user.get_balance()}")
        
        elif option == 4:
            amount = int(input("\tEnter Amount: "))
            user.take_loan(amount, bank)

        elif option == 5:
            print("\nOptions:")
            print("\n\t1. Deposite History")
            print("\t2. Withdraw History")
            print("\t3. Transfer History")
            print("\t4. Received Amount History")

            choice = int(input("\n\tEnter Choice: "))
            
            user.transactions(choice)
        
        elif option == 6:
            amount = int(input("\tEnter Amount: "))
            account_number = input("\tEnter Account Number: ")

            user.transfer_amount(amount, account_number, bank)
        
        elif option == 7:
            break

        else:
            print("\tInvalid Input!!")


# create user new account
def Create_new_account():
    print("\n\t\tCreate New Account:")
    print("\t  <---------------------------->\n")
    name = input("\tEnter Name: ")
    email = input("\tEnter Email: ")
    address = input("\tEnter address: ")
    account_type = input("\tEnter Account Type: ")
    password = input("\tEnter Password: ")

    user = User(name=name, email=email, address=address, account_type=account_type, password=password)
    bank.add_user(user)
    print("\n\tAccount Successfully Create!!")

    user_interface(user)

# login function
def login():
    name = input("\tEnter Name: ")
    email = input("\tEnter Email: ")
    password = input("\tEnter Password: ")

    account_number = name + email

    user = bank.find_account(account_number=account_number)

    if user:
        print("\n\t****Login Successfull****\n")
        user_interface(user)
    else:
        print("\n\tAccount does not exist!!")

# admin interface
def Admin_interface():
    while True:
        print("\n\t-----------------")
        print("\t  **Welcome**")
        print("\t-----------------\n")
        print("1. Create User Account")
        print("2. Remove User Account")
        print("3. View Users")
        print("4. View Available Balance")
        print("5. View Total Loan Amount")
        print("6. ON or OFF Loan Feature of Bank")
        print("7. Exit\n")

        option = int(input("Enter Option: "))

        if option == 1:
            print("\n\t****Create New Account****\n")
            name = input("\tEnter Name: ")
            email = input("\tEnter Email: ")
            address = input("\tEnter address: ")
            account_type = input("\tEnter Account Type: ")
            password = input("\tEnter Password: ")

            admin.create_account(name=name, email=email, address=address, account_type=account_type, password=password, bank=bank)
        
        elif option == 2:
            name = input("\tEnter Name: ")
            email = input("\tEnter Email: ")

            account_number = name + email

            admin.remove_account(account_number, bank)
        
        elif option == 3:
            admin.show_users(bank)

        elif option == 4:
            admin.check_available_balance(bank)
        
        elif option == 5:
            admin.check_loan_balance(bank)
        
        elif option == 6:
            choice = input("Enter Option (on/off): ")
            admin.on_off_loan_feature(choice.lower(), bank)

        elif option == 7:
            break
        
        else:
            print("\tInvalid Input!!")


while True:
    print("\nOptions:\n")
    print("1. User Login")
    print("2. Create Account")
    print("3. Admin Access")
    print("4. Exit\n")

    option = int(input("Enter Option: "))

    if option == 1:
        login()

    elif option == 2:
        Create_new_account()

    elif option == 3:
        Admin_interface()

    elif option == 4:
        break

    else:
        print("\n\tInvalid Input!!")