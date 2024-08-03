# composition provides "has a" relation

# example of computer

class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class Ram:
    def __init__(self, size) -> None:
        self.size = size

class PowerSupply:
    def __init__(self, watt) -> None:
        self.watt = watt

class HardDisk:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# computer has a cpu
# computer has a ram
# computer has a power supply
# computer has a hard disk
class Computer:
    def __init__(self, cores, ram_size, storage_capacity, watt) -> None:
        self.cores = CPU(cores)
        self.ram_size = Ram(ram_size)
        self.power_supply = PowerSupply(watt)
        self.storage_capacity = HardDisk(storage_capacity)
        pass