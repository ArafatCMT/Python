from abc import ABC
from orders import Order

class User(ABC): # Base class
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, Restaurent):
        Restaurent.menu.view_items()

    def add_to_cart(self, Restaurent, item_name, quentity):
        item = Restaurent.menu.find_item(item_name)
        if item:
            if quentity > item.quentity:
                print("\n\tItem quentity exceeded !")
            else:
                item.quentity = quentity
                self.cart.add_item(item)
                print("\n\t--> Item added")
        else:
            print("\n\tItem Not Found !")

    def view_cart(self):
        print("\n\tMy Cart:")
        print("\n\tName\tPrice\tQuentity")
        for item,quentity in self.cart.item.items():
            print(f"\t{item.name}\t{item.price}\t{item.quentity}")
        print(f"\n\t-->> Total Price: {self.cart.total_price}")

    def pay_bill(self):
        print(f"\n\tTotal {self.cart.total_price} Taka Paid Successlly !")
        self.cart.clear()



class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employees(self, Restaurent, employee): # ei employee and restaurent ak ta object
        Restaurent.add_employees(employee)

    def view_employees(self, Restaurent):
        Restaurent.view_employees()

    def add_new_item(self, Restaurent, item):
        Restaurent.menu.add_menu_item(item)

    def remove_item(self, Restaurent, item):
        Restaurent.menu.remove_item(item)
    
    def view_item(self, Restaurent):
        Restaurent.menu.view_items()
