from user import User
from order import Order

class Customer(User):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.cart = Order() # Cart holo Order class er ak ta Object
        
    def view_product(self, shopping):
        shopping.view_product()

    def add_to_cart(self, shopping, product_name, quentity):
        self.cart.add_to_cart(shopping, product_name, quentity)

    def show_cart(self):
        self.cart.view_cart()
    
    def remove_to_cart(self, shopping, product_name):
        self.cart.remove_to_cart(shopping, product_name)
    
    def BillPay(self):
        print(f"\n\tTotal Bill: {self.cart.total_price()} Taka Paid Successfully!!")
        self.cart.cart = {}