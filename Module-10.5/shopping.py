from product import Product

class Shopping:
    def __init__(self):
        self.products = {} #{"Apple" : product_object}
    
    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quentity += product.quentity
        else:
            self.products[product.name] = product
        
    def view_product(self):
        print("\t<----------------------------->")
        print("\tProduct List:\n")
        print("\tName\tPrice\tQuentity")
        for key,value in self.products.items():
            print(f"\t{key}\t{value.price}\t{value.quentity}")
        print("\t<----------------------------->")

    def find_product(self, product_name, quentity):
        if product_name in self.products:
            if quentity > self.products[product_name].quentity:
                print("\n\tNo Available Product!!\n")
                return None
            else:
                self.products[product_name].quentity -= quentity
                # create an object Product class
                name = self.products[product_name].name
                price = self.products[product_name].price
                product = Product(name, price, quentity)
                print("\n\tProduct Added to Cart!!\n")
                return product
        else:
            print("\n\tProduct Not Found!!\n")
            return None

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            print("\n\tProduct Removed!!")