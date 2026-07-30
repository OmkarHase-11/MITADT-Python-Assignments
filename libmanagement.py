class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []


library = Library()


def BookAddition():
    book_name = input("Enter the book name: ")
    author = input("Enter the author: ")

    new_book = Book(book_name, author)
    library.books.append(new_book)

    print("Book added successfully!")


def Registration():
    name = input("Enter your name: ")
    id = input("Enter your ID: ")

    new_patron = Patron(name, id)
    library.patrons.append(new_patron)

    print("Registration successful!")


def Borrowed():
    name = input("Enter the book name: ")

    for book in library.books:
        if book.book_name.lower() == name.lower():
            if book.available:
                print(f'"{book.book_name}" is available.')
            else:
                print(f'"{book.book_name}" is already borrowed.')
            return

    print("Book not found.")


while True:
    print("\n===== Library Menu =====")
    print("1. Add a Book")
    print("2. Register Patron")
    print("3. Check Book Availability")
    print("4. Exit")

    number = input("Enter your choice: ")

    if number == "1":
        BookAddition()

    elif number == "2":
        Registration()

    elif number == "3":
        Borrowed()

    elif number == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")