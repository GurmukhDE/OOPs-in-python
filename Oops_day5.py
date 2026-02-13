# OOP Example: Class and Object

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

# Creating object
emp1 = Employee("Rahul", 50000)

# Calling method
emp1.display_info()
