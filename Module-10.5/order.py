class Order:
    def __init__(self):
        self.cart = {} # {"apple": Product_Object}
    
    def add_to_cart(self, shopping, product_name, quentity):
        product = shopping.find_product(product_name, quentity)
        if product is not None:
            if product_name in self.cart:
                self.cart[product_name] += product.quentity
            else:
                self.cart[product_name] = product
                self.cart[product_name].quentity = quentity

    def remove_to_cart(self, shopping, product_name):
        if product_name in self.cart:
            quentity = self.cart[product_name].quentity
            del self.cart[product_name]
            print("\n\tRemove Product in Cart!!")
            shopping.products[product_name].quentity += quentity


    def view_cart(self):
        print("\t<----------------------------->")
        print("\tMy Cart:\n")
        print("\tName\tPrice\tQuentity")
        for key,value in self.cart.items():
            print(f"\t{key}\t{value.price}\t{value.quentity}")
        print(f"\n\tTotal Price: {self.total_price()} Taka!!")
        print("\t<----------------------------->")

    def total_price(self):
        return sum(value.price * value.quentity for key,value in self.cart.items())