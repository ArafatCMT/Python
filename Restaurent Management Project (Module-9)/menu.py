class Menu:
    def __init__(self):
        self.items = [] #items er data base

    def add_menu_item(self, item): # ei item ek ta object
        self.items.append(item)
        print("\n\t-->> Item added !")
    
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("\n\t-->> Item Deleted !")
        else:
            print("\n\t-->> Item Not Found !")

    def view_items(self):
        print("\n\tMenu:")
        print("\n\tName\tPrice\tQuentity")
        for item in self.items:
            print(f"\t{item.name}\t{item.price}\t{item.quentity}")