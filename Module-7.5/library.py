class Book:
    def __init__(self,name, isbn, available_copies):
        self.name = name
        self.isbn = isbn
        self.available_copies = available_copies

class Borrow_Book:
    def __init__(self, book_name, isbn, user_name, id):
        self.book_name = book_name
        self.isbn = isbn
        self.user_name = user_name
        self.id = id
        
class User:
    def __init__(self, name, id, password) -> None:
        self.name = name
        self.id = id
        self.password = password

class Library:
        def __init__(self, owner, name):
            self.owner = owner
            self.name = name
            self.book = []
            self.users = []
            self.borrow_book = []
        
        def add_book(self, name, isbn, available_copies):
            flag = False
            for book in self.book:
                if book.isbn == isbn:
                    flag = True
                    if available_copies > 0:
                        book.available_copies += available_copies
                    break
            if flag is False:
                book = Book(name, isbn, available_copies)
                self.book.append(book)
            print(f"\n\t-->> {book.name}, book {available_copies} copies added successfully !")
            print("\n\t<------------------------->")

        def add_user(self, name, id, password):
            flag = False
            for user in self.users:
                if user.id == id:
                    flag = True
                    print(f"\n\t-->> Id: {id} Already taken !")
            if flag is False:
                user = User(name, id, password)
                self.users.append(user)
                print("\n\t-->> Add user successfully !")
                return user


        def Borrow_book(self, book_name, isbn, user_name, user_id):
            match = False
            # check : is user member of libary
            for user in self.users:
                # condition true means user member of libary
                # print(user.name, user.id)
                if user_name == user.name and user_id == user.id:
                    match = True
                    flag = False
                    # check : is book exit in library
                    for book in self.book:
                        # condition true means book exit in libary
                        if book_name == book.name and isbn == book.isbn:
                            flag = True
                            check = False
                            for b_book in self.borrow_book:
                                if b_book.isbn == isbn and b_book.id == user_id:
                                    check = True
                                    print("\n\t-->> Already You Have Borrowed This Book !")
                                    break
                            if check is True:
                                break
                            elif book.available_copies >= 1:
                                print(f"\n\t-->> Borrow ({book_name}) Book Successfully !")
                                book.available_copies -= 1
                                BorrowBook = Borrow_Book(book_name, isbn, user_name, user_id)
                                self.borrow_book.append(BorrowBook)
                            else:
                                print("\n\t-->> No Available Copies")
                    if flag is False:
                        print("\n\t-->> No Book !")
            if match is False:
                print("\n\t-->> Without Library Member Can Not Borrow Book !")
            
        def show_books(self):
            print("\n\tBook List:")
            print("\n\tISBN\t\tName\t\tCopies")
            for book in self.book:
                print(f"\t{book.isbn}\t\t{book.name}\t{book.available_copies}")
            print("\n\t<------------------------->")
        
        def show_users(self):
            print("\n\tUsers:")
            print("\n\tName\t\tId")
            for user in self.users:
                print(f"\t{user.name}\t\t{user.id}")
            print("\n\t<------------------------->")
            
        
        def show_borrow_books(self):
            print("\n\tBorrow Book List:")
            print("\n\tISBN\t\tName\t\tUser_Name\t\tID")
            for obj in self.borrow_book:
                print(f"\t{obj.isbn}\t\t{obj.book_name}\t{obj.user_name}\t\t\t{obj.id}")
            print("\n\t<------------------------->")

        def demo_insert(self,name, isbn, available_copies):
            book = Book(name, isbn, available_copies)
            self.book.append(book)
        
        def registration(self, name, id, password):
            user = User(name, id, password)
            self.users.append(user)
            return user
            

bg = Library('Arafat', "Book Galaxcy")

bg.demo_insert("Omega Point", 102, 3)
bg.demo_insert("Chander Pahar", 549, 1)
bg.demo_insert("A Golden Age", 208, 8)
bg.demo_insert("Char Pata", 310, 2)

admin = bg.registration("Admin", 1, "admin")
arafat = bg.registration('Arafat', 101, "1234")
sumaiya = bg.registration('Sumaiya', 102, "2345")

currentUser = admin

while True:
    if currentUser == None:
        print("\n\t-->> No logged in user !!")

        option = input("Login ? Registration (L/R): ")

        if option == "R":
            id = int(input("\tEnter id: "))
            name = input("\tEnter name: ")
            password = input("\tEnter password: ")

            user = bg.registration(name, id , password)
            currentUser = user
            print("\n\t-->> Registration Successfull !")

        elif option == "L":
            id = int(input("\tEnter id: "))
            password = input("\tEnter password: ")
            match = False
            for user in bg.users:
                if user.id == id and user.password == password:
                    match = True
                    print("\n\t-->> Login Successfully !")
                    currentUser = user
                    break
            if match is False:
                print("\n\t-->> User not found !")

    elif currentUser == admin:
        print("Options:\n")
        print("1. Add Book")
        print("2. Add User")
        print("3. Show Users")
        print("4. Show All Books")
        print("5. Show Borrow Books List")
        print("6. Logout")

        option = int(input("Enter Option: "))

        if option == 1:
            id = int(input("\tEnter id: "))
            name = input("\tEnter name: ")
            cp = int(input("\tEnter copies: "))

            bg.add_book(name, id, cp)

        elif option == 2:
            id = int(input("\tEnter id: "))
            name = input("\tEnter name: ")
            password = input("\tEnter password: ")

            user = bg.add_user(name, id, password)

        elif option == 3:
            bg.show_users()

        elif option == 4:
            bg.show_books()

        elif option == 5:
            bg.show_borrow_books()
        elif option == 6:
            print("\n\t-->> Logout Successfully !")
            currentUser = None
    
    else:
        print("Options:\n")
        print("1. Show All Books")
        print("2. Borrow Book")
        print("3. return Book")
        print("4. Show Borrow Books")
        print("5. Logout")


        