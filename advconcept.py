
# OOP Concepts in Python

# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary      # Encapsulation

    def get_salary(self):
        return self.__salary

    def display(self):
        print("Name   :", self.name)
        print("Salary :", self.__salary)


# Child Class
class Manager(Employee):
    def __init__(self, name, salary, department, experience):
        super().__init__(name, salary)
        self.department = department
        self.experience = experience

    # Method Overriding
    def display(self):
        super().display()
        print("Department :", self.department)
        print("Experience :", self.experience, "Years")

        if self.experience >= 10:
            level = "Senior Manager"
        elif self.experience >= 5:
            level = "Manager"
        else:
            level = "Assistant Manager"

        print("Level      :", level)


# Another Child Class
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    # Method Overriding
    def display(self):
        super().display()
        print("Language :", self.language)


# -------- Main Program --------

print("====== Manager Details ======")
m1 = Manager("Amit", 75000, "Sales", 8)
m1.display()

print("\n====== Developer Details ======")
d1 = Developer("Neha", 55000, "Python")
d1.display()

print("\nSalary of Manager :", m1.get_salary())
