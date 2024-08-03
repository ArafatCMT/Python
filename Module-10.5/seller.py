from user import User

class Seller(User):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self, shopping, product): # product ak ta object
        shopping.add_product(product)
        print("\n\tProduct Added!!")
    
    def view_product(self, shopping):
        shopping.view_product()

    def remove_product(self, shopping, product_name):
        shopping.remove_product(product_name)