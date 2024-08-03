from user import User
from customer import Customer
from seller import Seller
from shopping import Shopping
from product import Product
from order import Order

# Create an Object Shopping Class
Golden_Basket = Shopping()

def login():
    print("Please Login:\n")
    print("1. Press 1 for Customer")
    print("2. Press 2 for Seller")
    choice = int(input("Enter Option: "))
    
    email = input("\tEnter Your Email: ")
    password = input("\tEnter Your Password: ")
    
    return email,password,choice

def Customer_Inerface(track):

    email = input("\tEnter Your Email: ")
    password = input("\tEnter Your Password: ")

    customer = Customer(email=email, password=password)

    if track != 1:
        Login = login()
        if Login[0] != email and Login[1] != password:
            return
        elif Login[2] == 2:
            print("\tYou Creat an Account Customer and Try to Login Seller!!")
            return

    while True:
        print("\n\t-------------------------")
        print("\t\tWelcome!!")
        print("\t-------------------------")
        print("Options:\n")
        print("1. Press 1 for view products")
        print("2. Press 2 for add to cart")
        print("3. Press 3 for view cart")
        print("4. Press 4 for remove product")
        print("5. Press 5 for Pay Bill")
        print("6. Press 6 for Main Page")

        option = int(input("\nEnter Option: "))

        if option == 1:
            customer.view_product(Golden_Basket)
        
        elif option == 2:
            product_name = input("\tEnter Product Name: ")
            quentity = int(input("\tEnter Product Quentity: "))

            customer.add_to_cart(Golden_Basket, product_name, quentity)
        
        elif option == 3:
            customer.show_cart()

        elif option == 4:
            product_name = input("\tEnter Product Name: ")
            customer.remove_to_cart(Golden_Basket, product_name)
        
        elif option == 5:
            customer.BillPay()

        elif option == 6:
            break
        
        else:
            print("\tInvalid Input")


def Seller_Interface(track):

    email = input("\tEnter Your Email: ")
    password = input("\tEnter Your Password: ")

    seller = Seller(email=email, password=password)

    if track != 1:
        Login = login()
        if Login[0] != email and Login[1] != password:
            return
        elif Login[2] == 1:
            print("\tYou Creat an Account Seller and Try to Login Customer !!")
            return
    
    while True:
        print("\n\t------------------------")
        print("\t\tWelcome!!")
        print("\t-------------------------")
        print("Options:\n")
        print("1. Press 1 for add products")
        print("2. Press 2 for view products")
        print("3. Press 3 for remove product")
        print("4. Press 4 for Main Page")

        option = int(input("\nEnter Option: "))

        if option == 1:
            product_name = input("\tEnter Product Name: ")
            price = int(input("\tEnter Price: "))
            quentity = int(input("\tEnter Product Quentity: "))

            product = Product(name=product_name, price=price, quentity=quentity)
            seller.add_product(Golden_Basket, product)

        elif option == 2:
            seller.view_product(Golden_Basket)

        elif option == 3:
            product_name = input("\tEnter Product Name: ")
            seller.remove_product(Golden_Basket, product_name)
        
        elif option == 4:
            break
        
        else:
            print("\tInvalid Input")


while True:
    print("\nMain Page:\n")
    print("1. Press 1 for Customer")
    print("2. Press 2 for Seller")
    print("3. Press 3 for Exit")

    option = option = int(input("\nEnter Option: "))

    if option == 1:
        Customer_Inerface(0)
    elif option == 2:
        Seller_Interface(0)
    elif option == 3:
        break
    else:
        print("\tInvalid Input")