class Shopping:

    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quentity):
        product = {'item' : item, 'price' : price, 'quentity' : quentity}
        self.cart.append(product)
    
    def checkOut(self, amount):

        total = 0

        for item in self.cart:
            # print(item)
            total += item['price'] * item['quentity']
        
        if amount < total:
            print(f'Give more : {total - amount} Taka')
        elif amount > total:
            extar = amount - total
            print(f'Here is your item, and extra money {extar} Taka')
        else:
            print(f'Here is your item')

    def item_remove(self, item, quentity = 0):
        
        if quentity == 0:
            # search item to remove
            for i in self.cart:
                # print(i['item'])
                if i['item'] == item:
                    self.cart.remove(i)
        
        else:
            for i in self.cart:
                if i['item'] == item:
                    i['quentity'] = i['quentity'] - quentity
        for i in self.cart:
            print(i)
        
            
sakib = Shopping('sakib')
sakib.add_to_cart('Potato', 40, 4)
sakib.add_to_cart('Onion', 80, 5)
sakib.add_to_cart('Tomato', 60, 3)
sakib.add_to_cart('Oil', 120, 5)

# sakib.checkOut(100)
# sakib.checkOut(1500)
# sakib.checkOut(1340)
# print(sakib.cart)

# sakib.item_remove('Tomato')
# sakib.checkOut(1500)

sakib.item_remove('Tomato',2)
sakib.checkOut(1500)