class Shop:

    # constractor
    def __init__(self, buyer):
        self.buyer = buyer
        self.receipt = [] # instance attribute

    def add_to_receipt(self, item, price):
        self.receipt.append((item,price))
    
Kabila = Shop('Kabila')
Kabila.add_to_receipt('Watch', 3200)
Kabila.add_to_receipt('T-shirt', 1500)

print(Kabila.buyer, Kabila.receipt)


Sabbir = Shop('Sabbir')
Sabbir.add_to_receipt('Shoe', 2200)
Sabbir.add_to_receipt('Water Bottle', 500)
print(Sabbir.buyer, Sabbir.receipt)