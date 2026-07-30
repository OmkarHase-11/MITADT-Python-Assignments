class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def get_salary_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("-" * 40)
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      : ₹", format(self.salary, ".2f"))
        print("Category    :", self.get_salary_category())


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def employee_exists(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return True
        return False

    def add_employee(self):
        employee_id = input("Enter Employee ID: ").strip()

        if self.employee_exists(employee_id):
            print("Employee ID already exists.\n")
            return

        name = input("Enter Employee Name: ").strip()

        try:
            salary = float(input("Enter Employee Salary: ₹"))

            if salary < 0:
                print("Salary cannot be negative.\n")
                return

        except ValueError:
            print("Please enter a valid salary.\n")
            return

        employee = Employee(employee_id, name, salary)
        self.employees.append(employee)

        print("Employee added successfully!\n")

    def display_all_employees(self):
        if not self.employees:
            print("No employee records found.\n")
            return

        print("\n" + "=" * 40)
        print("Company:", self.company_name)
        print("EMPLOYEE INFORMATION")
        print("=" * 40)

        for employee in self.employees:
            employee.display()

        print("-" * 40)
        print()

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ").strip()

        for employee in self.employees:
            if employee.employee_id == employee_id:
                print("\nEmployee found:")
                employee.display()
                print()
                return

        print("Employee not found.\n")


def main():
    company_name = input("Enter Company Name: ").strip()
    company = Company(company_name)

    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            company.add_employee()

        elif choice == "2":
            company.display_all_employees()

        elif choice == "3":
            company.search_employee()

        elif choice == "4":
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Please try again.\n")


main()
