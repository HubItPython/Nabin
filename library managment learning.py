
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
               
            
