from bus_management_system import Bus, BusCompany

company = BusCompany("C Line")

while True:
    print("\nWelcom to Bus Ticket Booking System!!")
    print("1. Install Bus")
    print("2. View Available Bus")
    print("3. Booked Ticket")
    print("4. Check Seat Status")
    print("5. Exit")

    option = int(input("Enter Option: "))

    if option == 1:
        coach = int(input("Enter Coach Number: "))
        driver = input("Enter Driver Name: ")
        arival = input("Enter Bus Arival Time: ")
        departure = input("Enter Bus Departure Time: ")
        from_des = input("Enter Bus Destination: ")
        to = input("Enter Bus to Destination: ")

        bus = Bus(coach, driver, arival, departure, from_des, to)
        company.install_bus(bus)

    elif option == 2:
        company.display_available_buses()

    elif option == 3:
        coach = int(input("Enter Coach Number: "))
        row = int(input("Enter Row Number: "))
        col = int(input("Enter Col Number: "))

        company.book_ticket(coach, row, col)
    
    elif option == 4:
        coach = int(input("Enter Coach Number: "))
        company.display_seat_status(coach)
    
    elif option == 5:
        break

    else:
        print("Invalid Input!!")