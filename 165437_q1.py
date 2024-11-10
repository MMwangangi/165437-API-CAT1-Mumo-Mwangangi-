# Book class definition
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

# LibraryMember class definition
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Interactive Code
if __name__ == "__main__":
    # Creating sample books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    # Creating a library member
    member = LibraryMember("Alice", 1)

    # Interactive borrowing and returning
    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            book_title = input("Enter the title of the book you want to borrow: ")
            if book_title == "The Great Gatsby":
                member.borrow_book(book1)
            elif book_title == "To Kill a Mockingbird":
                member.borrow_book(book2)
            elif book_title == "1984":
                member.borrow_book(book3)
            else:
                print("Book not found.")

        elif choice == "2":
            book_title = input("Enter the title of the book you want to return: ")
            if book_title == "The Great Gatsby":
                member.return_book(book1)
            elif book_title == "To Kill a Mockingbird":
                member.return_book(book2)
            elif book_title == "1984":
                member.return_book(book3)
            else:
                print("Book not found.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")
