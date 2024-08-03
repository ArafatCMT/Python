class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.item_list = []
        pass

    def add_product(self, product_name, quentity, price):
        product = Product(product_name, quentity, price)
        self.item_list.append(product)

    def buy_product(self, product_name, quentity):
        flag = False

        for item in self.item_list:
            # print(f'name : {item.product_name} , quentity : {item.quentity} , price : {item.price}')
            if item.product_name == product_name:
                if quentity <= item.quentity:
                    item.quentity -= quentity
                    self.bill_calculate(item.price, quentity)
                    flag = True
        if flag is True:
            print("Congress ! you have successfully buy a product.")
        else:
            print("Sorry, product not available.")

    def bill_calculate(self, price, quentity):
        total = price * quentity
        print(f"Please pay the bill : {total} taka.")
        taka = int(input("Buyer : "))

        if taka < total:
            print(f"Give more : {total - taka} taka.")
            t = int(input("Buyer : "))
            if total == taka + t:
                print("Thanks.")

        elif taka > total:
            print(f"Here it : {taka - total} taka.")
            # print("Thanks.")
        else:
            print("Thanks.")
            

class Product:
    def __init__(self, product_name, quentity, price) -> None:
        self.product_name = product_name
        self.price = price
        self.quentity = quentity


obj = Shop('Golden Basket')
obj.add_product('tomato', 2, 20)
obj.add_product('potato', 3, 30)
obj.add_product('onion', 2, 40)

# obj.buy_product('tomato', 2)
# obj.buy_product('potato', 2)


obj2= Shop('Big Bazar')
obj2.add_product('garlic', 5, 80)
obj2.add_product('Apple', 3, 230)
obj2.add_product('onion', 2, 40)

# obj.buy_product('tomato', 2)
obj2.buy_product('Apple', 2)