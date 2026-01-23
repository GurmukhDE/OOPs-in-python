
"""Understand this clearly:
class → blueprint
self → current object
__init__ → constructor (runs automatically)
method → function inside class"""




class Employee:
    def __init__(self, name, salary):
        self.name = name        # data
        self.salary = salary    # data

    def yearly_salary(self):
        return self.salary * 12   # logic


# object creation
emp1 = Employee("Rahul", 50000)

print(emp1.name)
print(emp1.yearly_salary())
