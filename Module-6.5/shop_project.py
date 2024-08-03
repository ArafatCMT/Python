class Product:
    def __init__(self, product_name, product_id, price) -> None:
        self.product_name = product_name # product class er access modifier : public
        self.product_id = product_id
        self.price = price

    def add_product(self, product_id, quentity):
        self.quentity = quentity
 

class Shop:
    # class attribute
    item_lst = []

    def __init__(self,) -> None:
        # self.name = name
        pass

    def buy_product(self, product_name, quentity):
        flag = False

        # check product is available or not

        for obj in self.item_lst:
            # print(obj.product_name, obj.product_id, obj.quentity)

            if obj.product_name == product_name:

                if quentity <= obj.quentity:
                    obj.quentity = obj.quentity - quentity
                    flag = True

        if flag is False:
            print("Sorry, product not available.")
        else:
            print("Congress, you have successfully buy a product.")


            
shop = Shop()

tomato = Product("Tomato", 101, 40)
tomato.add_product(101, 8)
shop.item_lst.append(tomato)

potato = Product("Potato", 102, 50)
potato.add_product(102, 10)
shop.item_lst.append(potato)

onion = Product("Onion", 103, 90)
onion.add_product(103, 9)
shop.item_lst.append(onion)

garlic = Product("Garlic", 104, 70)
garlic.add_product(104, 6)
shop.item_lst.append(garlic)

apple = Product("Apple", 105, 220)
apple.add_product(105, 7)
shop.item_lst.append(apple)

orange = Product("Orange", 106, 230)
orange.add_product(106, 5)
shop.item_lst.append(orange)



rahim = Shop()
rahim.buy_product("Apple", 5)

karim = Shop()
karim.buy_product("Apple", 3)