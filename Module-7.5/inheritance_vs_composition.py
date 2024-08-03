# inheritance provides "is a" realtion
# example inheritance
class Animal:
    def __init__(self) -> None:
        pass

    def move(self):
        print("move with four legs")

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

class Tiger(Animal):
    def __init__(self) -> None:
        super().__init__()

# composition provides "has a" realtion
# example com

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
        pass

class Battary:
    def __init__(self, ampere) -> None:
        self.ampere = ampere
        pass

class Processor:
    def __init__(self, name) -> None:
        self.name = name
        pass

class Display:
    def __init__(self, quality) -> None:
        self.quality = quality
        pass

# phone has a camera
# Phone has a battary
# Phone has a processor
# Phone has a display
class Phone:
    def __init__(self, brand, model, price, pixel, battary_amp, processor, quality) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.pixel = Camera(pixel)
        self.battary = Battary(battary_amp)
        self.processor = Processor(processor)
        self.Display = Display(quality)
        pass