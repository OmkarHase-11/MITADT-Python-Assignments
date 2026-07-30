import csv

FILENAME = "SY_students.csv"


# Decorator given in the PDF
def report_header(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print("            STUDENT REPORT")
        print("=" * 40)

        result = func(*args, **kwargs)

        print("=" * 40 + "\n")
        return result

    return wrapper


class Report:
    college = "ABC Engineering College"

    # Constructor / Magic Method
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Class Method
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name
        print("College name changed successfully!\n")

    # Magic Method
    def __str__(self):
        return (
            f"Name    : {self.name}\n"
            f"Roll No : {self.roll}\n"
            f"Marks   : {self.marks}"
        )

    # Decorator applied to the report
    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)

        if self.marks >= 40:
            print("Result  : PASS")
        else:
            print("Result  : FAIL")


def add_student():
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()

    try:
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.\n")
            return

    except ValueError:
        print("Please enter valid numerical marks.\n")
        return

    # Check whether the roll number already exists
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0] == roll:
                    print("A student with this roll number already exists.\n")
                    return

    except FileNotFoundError:
        pass

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student record added successfully!\n")


def view_students():
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            records_found = False

            for row in reader:
                if len(row) >= 3:
                    records_found = True

                    student = Report(
                        name=row[1],
                        roll=row[0],
                        marks=float(row[2])
                    )

                    student.display_report()

            if not records_found:
                print("No student records found.\n")

    except FileNotFoundError:
        print("No records found. Please add students first.\n")


def search_student():
    roll = input("Enter Roll Number to search: ").strip()
    found = False

    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 3 and row[0] == roll:
                    student = Report(
                        name=row[1],
                        roll=row[0],
                        marks=float(row[2])
                    )

                    student.display_report()
                    found = True
                    break

        if not found:
            print(f"No record found for Roll Number: {roll}\n")

    except FileNotFoundError:
        print("No records found. Please add students first.\n")


def update_college():
    new_college = input("Enter the new college name: ").strip()

    if new_college:
        Report.change_college(new_college)
    else:
        print("College name cannot be empty.\n")


def menu():
    while True:
        print("===== Class SY Student Management =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Change College Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_college()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


menu()
