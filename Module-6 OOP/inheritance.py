# base class , parent class , common attributes + functionality class
# derived class, child class, uncommon attributes + functionality class

class Device:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price 
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running Start : {self.brand}'
    
    def __repr__(self) -> str:
        return f'Features : {self.brand} {self.price } {self.color} {self.origin}'

class Laptop:
    def __init__(self, ssd, ram) -> None:
        self.ssd = ssd
        self.ram = ram

    def coding(self):
        return f'Learning python and practiceing'
    
class Phone(Device):
    def __init__(self, brand, price, color, origin, memory, ram, dual_sim) -> None:
        self.memory = memory
        self.ram = ram
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def __repr__(self) -> str:
        return f'{self.memory} , {self.ram} , {self.dual_sim}'

    def phone_call(self, number, text):
        return f'sending sms to : {number} with : {text}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
    
    def change_lens(self):
        pass

my_phone = Phone('Walton', 12000, 'Black', 'Bangladesh', '256GB', '16GB', 'Support')
print(my_phone.brand, my_phone.price, my_phone)



        