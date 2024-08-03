from abc import ABC

class User(ABC):
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

        


# s = Shopping()
# item = Product("Apple", 10, 20)
# item1 = Product("Orange", 15, 25)
# s.add_product(item)
# # s.view_product()
# s.add_product(item1)
# # s.view_product()
# item3 = Product("Apple", 10, 50)
# s.add_product(item3)
# # s.view_product()
# cus = Customer("afraft", 1234)
# cus.view_product(s)

# cus.add_to_cart(s, "Apple", 10)
# cus.add_to_cart(s, "Orange", 20)
# cus.view_product(s)
# cus.show_cart()





# cus.remove_to_cart(s,"Apple")
# cus.show_cart()
# cus.BillPay()
# cus.show_cart()
# cus.view_product(s)

# # cus.view_product(s)
# # sel = Seller("afraft", 1234)

# # sel.remove_product(s,"Apple")
# s.view_product()
# print(s.products[product_name])
