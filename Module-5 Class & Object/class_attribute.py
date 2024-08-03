class Shop:

    # class attribute
    receipt = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_receipt(self, item, price):
        self.receipt.append((item,price))

Farhan = Shop('Farhan')
Farhan.add_to_receipt('Sun Glass', 1200)
Farhan.add_to_receipt('Wallet', 2000)

print(Farhan.receipt)

Payel = Shop('Payel')
Payel.add_to_receipt('Phone', 32000)
Payel.add_to_receipt('Dress', 4500)
print(Payel.receipt)