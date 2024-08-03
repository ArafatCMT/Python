class Order:
    def __init__(self) -> None:
        self.item = {}

    def add_item(self, item):
        if item in self.item:
            self.item[item] += item.quentity # jodi item ta cart e thake
        else:
            self.item[item] = item.quentity # jodi item ta cart e na thake
    
    def remove_item(self, item):
        if item in self.item:
            del self.item[item]
            print("\n\t--> Item removed !")
    @property
    def total_price(self):
        return sum(item.price * quentity for item,quentity in self.item.items())

    def clear(self):
        self.item = {}