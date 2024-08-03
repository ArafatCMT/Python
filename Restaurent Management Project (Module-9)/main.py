from users import Customer, Employee, Admin
from restaurent import Restaurent
from orders import Order
from menu import Menu 
from food_item import FoodItem

mamar_restaurent = Restaurent("Mamar Restaurent")

def Customer_interface():
    name = input("\tEnter Name: ")
    email = input("\tEnter Email: ")
    phone = input("\tEnter Phone: ")
    address = input("\tEnter Address: ")

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print("\t------------------------------")
        print(f"\t\tWelcome {customer.name}")
        print("\t------------------------------")
        print("Options:\n")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer.view_menu(mamar_restaurent)

        elif choice ==  2:
            name = input("\tEnter Item Name: ")
            quentity = int(input("\tEnter Item Quentity: "))

            customer.add_to_cart(mamar_restaurent, name, quentity)

        elif choice == 3:
            customer.view_cart()
        
        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break
        else: 
            print("\n\t-->> Invalid Input !")

def Admin_interface():
    name = input("\tEnter Name: ")
    email = input("\tEnter Email: ")
    phone = input("\tEnter Phone: ")
    address = input("\tEnter Address: ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print("\t------------------------------")
        print(f"\t\tWelcome {admin.name}")
        print("\t------------------------------")
        print("Options:\n")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View item")
        print("5. Remove item")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            # add item
            item_name = input("\tEnter item name: ")
            item_price = int(input("\tEnter item price: "))
            item_quentity = int(input("\tEnter item quentity: "))
            item = FoodItem(item_name, item_price, item_quentity)

            admin.add_new_item(mamar_restaurent, item)

        elif choice ==  2:
            # add employee
            name = input("\tEnter Name: ")
            email = input("\tEnter Email: ")
            phone = input("\tEnter Phone: ")
            address = input("\tEnter Address: ")
            age = input("\tEnter Age: ")
            designation = input("\tEnter Designation: ")
            salary = input("\tEnter Salary: ")

            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employees(mamar_restaurent, employee)

        elif choice == 3:
            # view employee
            admin.view_employees(mamar_restaurent)
        
        elif choice == 4:
            # view menu
            admin.view_item(mamar_restaurent)

        elif choice == 5:
            # remove item
            item_name = input("\tEnter Item Name: ")
            admin.remove_item(mamar_restaurent, item_name)
        elif choice == 6:
            break
        else: 
            print("\n\t-->> Invalid Input !")
    

while True:
    print("\t----------------------------------------")
    print(f"\t\tWelcome {mamar_restaurent.name}!!")
    print("\t----------------------------------------")
    print("Options:\n")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        Customer_interface()

    elif choice == 2:
        Admin_interface()
    
    elif choice == 3:
        break

    else:
        print("\n\t-->> Invalid Input !")
