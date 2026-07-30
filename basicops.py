import csv
FILENAME = "SY_students.csv"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, marks])
    print("Student record added successfully!\n")

def view_students():
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            print("\n--- Student Records ---")
            for row in reader:
                print("Roll:", row[0], "| Name:", row[1], "| Marks:", row[2])
            print("-----------------------\n")
    except FileNotFoundError:
        print("No records found. Please add students first.\n")

def search_student():
    roll = input("Enter Roll Number to search: ")
    found = False
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == roll:
                    print("Record Found -> Roll:", row[0], "| Name:", row[1], "| Marks:", row[2])
                    found = True
                    break
        if not found:
            print("No record found for Roll Number:", roll)
    except FileNotFoundError:
        print("No records found.\n")

def menu():
    while True:
        print("===== Class SY Student Management =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
menu()