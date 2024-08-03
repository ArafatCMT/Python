from abc import ABC

class AbstractBus(ABC):
    def __init__(self, coach, driver, arival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arival = arival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seats = [[0 for j in range(0,4)] for i in range(0,10)]

class Bus(AbstractBus):
    pass

class BusCompany:
    def __init__(self, name):
        self.name = name
        self.buses = {}

    def install_bus(self, bus):
        print(f"\nBus : Coach Number {bus.coach} is Added Successfully!!")
        self.buses[bus.coach] = bus

    def display_available_buses(self):
        if not self.buses:
            print("\nNo Buses are Available!!")
        else:
            print("\n\tCoach\tDriver\tArival\tDeparture\tFrom\tTo")
            
            for coach,bus in self.buses.items():
                print(f"\t{coach}\t{bus.driver}\t{bus.arival}\t{bus.departure}\t{bus.from_des}\t{bus.to}")

    def book_ticket(self, coach, row, col):
        if coach in self.buses:
            if (row >= 0 and row < 10 and col >= 0 and col < 4):
                if self.buses[coach].seats[row][col] == 0:
                    print(f"\nSeat {row,col} Booked Successfully!!")
                    self.buses[coach].seats[row][col] = 1
                else:
                    print("\nSeat Already Booked!!")
            else:
                print("\nInvalid Seat!!")
        else:
            print("\nInvalid Bus Coach Number!!")

    def display_seat_status(self, coach):
        if coach in self.buses:
            lst = []
            for i in range(0,10):
                for j in range(0,4):
                    lst.append(self.buses[coach].seats[i][j])
                print(lst)
                lst = []
        else:
            print("\nInvalid Bus Coach Number!!")




