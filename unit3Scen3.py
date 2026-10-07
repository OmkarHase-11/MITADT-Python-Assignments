import csv
import re

books = []

# Read books from CSV file
try:
    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            books.append(row)

except FileNotFoundError:
    print("books.csv file not found.")
    exit()


# Display all books
print("\n--- Book Records ---")

for book in books:
    print("Book ID :", book["BookID"])
    print("Title   :", book["Title"])
    print("Author  :", book["Author"])
    print("Price   :", book["Price"])
    print("--------------------")


# Get keyword from user
keyword = input("\nEnter starting keyword of book title: ")

# Regular expression
pattern = re.compile("^" + re.escape(keyword), re.IGNORECASE)

print("\n--- Matching Books ---")

found = False

for book in books:

    if pattern.search(book["Title"]):

        print("Book ID :", book["BookID"])
        print("Title   :", book["Title"])
        print("Author  :", book["Author"])
        print("Price   :", book["Price"])
        print("--------------------")

        found = True


if not found:
    print("No matching books found.")
