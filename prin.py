# # # def a():
# # #     print("a")
# # # def b():
# # #     return a
# # # c=b()
# # # c()


# # # a=[1]
# # # a.extend([2,3,4,5])
# # # a.append([2,3,4,5,6])
# # # print(a)


# # # def a(n):
# # #     if (n==0):
# # #         return
# # #     print(n)
# # #     a(n-1)
# # #     print("End")
# # # a(5)


# # # # lamda is a small anonymous functtion defined in sigle lineup code  only anonymous if variable is defined in lambda
# # # # syntax  = lamda arguments : expression
# # # l = lambda x,y:x+y
# # # y=l(2,4)
# # # print(y)
# # import pyttsx3 as p

# # engine = p.init()
# # voices = engine.getProperty('voices')

# # # Print out the number of voices available
# # print("Number of voices available:", len(voices))

# # # Print out details of each voice
# # for idx, voice in enumerate(voices):
# #     print(f"Voice {idx}:")
# #     print(" - ID:", voice.id)
# #     print(" - Name:", voice.name)
# #     print(" - Languages:", voice.languages)
# #     print(" - Gender:", voice.gender)
# #     print(" - Age:", voice.age)
# #     print()

# list=[2+3]
# print(list)



# types of attributes 
# classs attributes
# instance attributes 
# class student():
#     def __init__(self,name,a,b,c):
#         self.__name=name
#         self.a=a
#         self.b=b
#         self.c=c
#     def average(self):
#         print("name:",self.__name,"Average:",(self.a+self.b+self.c)/3)
# n=str(input("enter yourname: "))
# g=int(input("enter sub1 number: "))
# h=int(input("enter sub2 number: "))
# k=int(input("enter sub3 number: "))
# a = student(n,g,h,k)
# a.average()

# a = student("",1,2,3)
# a.average("nabin",1,2,3)
# a = student("nabin",1,2,3)
# a.average("nabin",1,2,3)

# class Bank:
#     def __init__(self):
#         self.__balance = 0
#         self.__pin = ""
#         self.__name = ''
#         self.menu()

#     def menu(self):
#         print("""Processed according to Your Choice :
#              press 1 to create pin 
#              press 2 to withdraw 
#              press 3 to deposit
#              press 4 to see balance
#              press 5 to transfer balance 
#              press 6 to exit 
#                    """) 
#         take = int(input())
#         if take == 1:
#             self.create()
#         elif take == 2:
#             self.withdraw()
#         elif take == 3:
#             self.deposit()
#         elif take == 4:
#             self.check()
#         elif take == 5:
#             self.transfer()
#         elif take == 6:
#             self.exit()

#     def create(self):
#         self.__name = input("Enter account holder name: ")
#         self.__pin = input("Enter your new PIN: ")
#         print("PIN created successfully")
#         self.menu()

#     def deposit(self):
#         temp = input("Enter your username: ")
#         tempp = input("Enter your PIN number kindly: ")
#         if self.__name == temp and self.__pin == tempp:
#             print("Authentication successful")
#             amount = float(input("Enter amount to deposit: "))
#             self.__balance += amount
#             print(f"Deposit of {amount} successful. Your new balance is {self.__balance}")
#         else:
#             print("Invalid username or PIN")
#         self.menu()

#     def withdraw(self):
#         temp = input("Enter your username: ")
#         tempp = input("Enter your PIN number kindly: ")
#         if self.__name == temp and self.__pin == tempp:
#             print("Authentication successful")
#             amount = float(input("Enter amount to withdraw: "))
#             if self.__balance >= amount:
#                 self.__balance -= amount
#                 print(f"Withdrawal of {amount} successful. Your new balance is {self.__balance}")
#             else:
#                 print("Insufficient balance")
#         else:
#             print("Invalid username or PIN")
#         self.menu() 

#     def check(self, other_account=None):
#         print(f'Your account has {self.__balance} Balance')
#         if other_account:
#            print(f'{other_account.name} account has {other_account.__balance} Balance')
#         self.menu()
       

#     def exit(self):
#         print("Exiting program.")

#     def transfer(self):
#         temp = input("Enter your username: ")
#         tempp = input("Enter your PIN number: ")
#         if self.__name == temp and self.__pin == tempp:
#             print("Authentication successful")
#             recipient = input("Enter recipient's username: ")
#             amount = float(input("Enter amount to transfer: "))
#             if self.__balance >= amount:
#                 self.__balance -= amount
#                 other_account = input("Enter recipient's account holder name: ")
#                 print(f"Transfer of {amount} to {recipient} successful.")
#                 print(f"Your new balance is {self.__balance}")
#                 return amount, other_account
#             else:
#                 print("Insufficient balance")
#         else:
#             print("Invalid username or PIN")
#         self.menu()

# # Instantiate objects
# a = Bank()
# b = Bank()

# # Perform transfer from a to b
# amount, other_account = a.transfer()
# if other_account == b.__name:
#     b.__balance += amount
#     print(f"Transfer of {amount} from {a.__name} to {b.__name} successful.")
#     print(f"{b.__name}'s new balance is {b.__balance}")



# class Bank_Management():
#     def __init__(self, name, balance) -> None:
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Your account has been Debited by {amount}')
#         print(f'Your Remaining Balance is {self.balance}')

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f'Your account has been Credited by {amount}')
#             print(f'Your Remaining Balance is {self.balance}')
#         else:
#             print("Insufficient funds")

#     def check_balance(self, other_account=None):
#         print(f'Your account has {self.balance} Balance')
#         if other_account:
#             print(f'{other_account.name} account has {other_account.balance} Balance')

#     def transfer_funds(self, other_account, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             other_account.balance += amount
#             print(f'Funds transferred successfully to {other_account.name}')
#         else:
#             print("Insufficient funds for transfer")


# def f(account_holder, account_holder2):
#     obj = Bank_Management(account_holder, 500)
#     obj2 = Bank_Management(account_holder2, 1000)
    
#     while True:
#         inp = int(input('''
#              Enter 1 to deposit
#              Enter 2 for Withdraw
#              Enter 3 for checking balance
#              Enter 4 to Transfer Funds
#         '''))
        
#         if inp == 1:
#             amounts = int(input('Enter Amount\n'))
#             obj.deposit(amounts)
#         elif inp == 2:
#             amounts = int(input('Enter Amount\n'))
#             obj.withdraw(amounts)
#         elif inp == 3:
#             obj.check_balance(obj2)  # Pass obj2 to check_balance method
#         elif inp == 4:
#             amounts = int(input('Enter Amount\n'))
#             obj.transfer_funds(obj2, amounts)
#         else:
#             print('Wrong Input')

# account_holder = input('Enter Account Holder Name\n')
# account_holder2 = input('Enter Account Holder Name for Account 2\n')

# f(account_holder, account_holder2)

# Online Shopping System:
# Scenario: You are tasked with creating a system to handle online shopping for a retail company.

# Question: Develop a class hierarchy to represent different types of products available for purchase, including attributes and methods for managing inventory, pricing, and handling orders.

# class MarketItem:
#     def __init__(self, item, price, quantity):
#         self.__item = item
#         self.__price = price
#         self.__quantity = quantity

#     def set_price(self, new_price):
#         self.__price = new_price

#     def set_quantity(self, quantity_change):
#         self.__quantity += quantity_change

#     def get_info(self):
#         return f"Name: {self.__item}\nPrice: ${self.__price}\nQuantity: {self.__quantity}"


# class Product:
#     def __init__(self, name, price, quantity, category):
#         self.market_item = MarketItem(name, price, quantity)
#         self.category = category

#     def get_info(self):
#         return self.market_item.get_info() + f"\nCategory: {self.category}"

#     def set_price(self, new_price):
#         self.market_item.set_price(new_price)

#     def set_quantity(self, quantity_change):
#         self.market_item.set_quantity(quantity_change)


# def main():
#     product = Product(input("Enter product name: "),
#                       float(input("Enter price: ")),
#                       int(input("Enter quantity: ")),
#                       input("Enter category: "))

#     print(product.get_info())

#     while True:
#         print("""Choose action to perform:
#             1. Update quantity
#             2. Update price
#             3. Add new item
#             4. Exit""")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             quantity_change = int(input("Enter quantity change: "))
#             product.set_quantity(quantity_change)
#             print(product.get_info())

#         elif choice == "2":
#             new_price = float(input("Enter new price: "))
#             product.set_price(new_price)
#             print(product.get_info())

#         elif choice == "3":
#             new_product = Product(input("Enter product name: "),
#                                   float(input("Enter price: ")),
#                                   int(input("Enter quantity: ")),
#                                   input("Enter category: "))
#             print(new_product.get_info())

#         elif choice == "4":
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()

from datetime import datetime

class Book:
    def __init__(self, book_id, title, total_copies):
        self.book_id = book_id
        self.title = title
        self.total_copies = total_copies
        self.available_copies = total_copies

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

class BorrowingRecord:
    def __init__(self, book, patron):
        self.book = book
        self.patron = patron
        self.checked_out_date = datetime.now()
        self.returned_date = None

    def return_book(self):
        self.returned_date = datetime.now()
        self.patron.borrowed_books.remove(self)

class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}
        self.borrowing_records = []

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_patron(self, patron):
        self.patrons[patron.patron_id] = patron

    def check_out_book(self, book_id, patron_id):
        book = self.books.get(book_id)
        patron = self.patrons.get(patron_id)
        if book and patron and book.available_copies > 0:
            borrowing_record = BorrowingRecord(book, patron)
            self.borrowing_records.append(borrowing_record)
            patron.borrowed_books.append(borrowing_record)
            book.available_copies -= 1
            return borrowing_record, book.available_copies
        print("\nAvailable Books:")
        for book_id, book in self.books.items():
            print(f"Book ID: {book_id}, Title: {book.title}, Available Copies: {book.available_copies}")

        print("\nBorrowing Details:")
        for record in self.borrowing_records:
            print(f"Book '{record.book.title}' borrowed by {record.user.name}")

        return borrowing_record, book.available_copies
    
    
    def return_book(self, book_id, patron_id):
        for record in self.borrowing_records:
            if record.book.book_id == book_id and record.patron.patron_id == patron_id and record.returned_date is None:
                returned_record = record
                record.return_book()
                record.book.available_copies += 1
    
                print(f"\nBook '{returned_record.book.title}' returned by {returned_record.patron.name}")

                print("\nAvailable Copies:")
                for book_id, book in self.books.items():
                    print(f"Book ID: {book_id}, Title: {book.title}, Available Copies: {book.available_copies}")
    
                return returned_record, record.book.available_copies
    
if __name__ == "__main__":
    library = Library()
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                book_id = input("Enter book ID: ")
                title = input("Enter book title: ")
                total_copies = int(input("Enter total copies: "))
                book = Book(book_id, title, total_copies)
                library.add_book(book)
                patron_id = input("Enter patron ID: ")
                name = input("Enter patron name: ")
                patron = Patron(patron_id, name)
                library.add_patron(patron)
                add_more = input("Do you want to add another book? (yes/no): ")
                if add_more.lower() != 'yes':
                    break
        if choice == "2":
            while True:
                book_id = input("Enter book ID to borrow: ")
                patron_id = input("Enter patron ID: ")
                borrowing_record, available_copies = library.check_out_book(book_id, patron_id)
                if borrowing_record:
                    print(f"Book '{borrowing_record.book.title}' borrowed by {borrowing_record.patron.name}")
                    print(f"Available copies of '{borrowing_record.book.title}': {available_copies}")
                else:
                    print("Book not available or invalid book/patron ID.")
                add_more = input("Do you want to borrow another book? (yes/no): ")
                if add_more.lower() != 'yes':
                    break

        elif choice == "3":
            while True:
                book_id = input("Enter book ID to return: ")
                patron_id = input("Enter patron ID: ")
                returning_record, available_copies = library.return_book(book_id, patron_id)
                if returning_record:
                    print(f"Book '{returning_record.book.title}' returned by {returning_record.patron.name}")
                    print(f"Available copies of '{returning_record.book.title}': {available_copies}")
                else:
                    print("No matching borrowing record found or the book has already been returned.")
                add_more = input("Do you want to return another book? (yes/no): ")
                if add_more.lower() != 'yes':
                    break

        elif choice == "4":
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
               
            