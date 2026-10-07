import csv
import sys

# Check command-line argument
if len(sys.argv) != 2:
    print("Usage: python employee.py <filename>")
    sys.exit()

filename = sys.argv[1]

employees = []

# Read CSV file
try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)

except FileNotFoundError:
    print("File not found.")
    sys.exit()


# Display all employee details
print("\n--- Employee Records ---")

for employee in employees:
    print("Employee ID :", employee["EmployeeID"])
    print("Name        :", employee["Name"])
    print("Department  :", employee["Department"])
    print("Salary      :", employee["Salary"])
    print("------------------------")


# Search employee by ID
search_id = input("\nEnter Employee ID to search: ")

found = False

for employee in employees:
    if employee["EmployeeID"] == search_id:
        print("\nEmployee Found:")
        print("Employee ID :", employee["EmployeeID"])
        print("Name        :", employee["Name"])
        print("Department  :", employee["Department"])
        print("Salary      :", employee["Salary"])

        found = True
        break

if not found:
    print("Employee not found.")
