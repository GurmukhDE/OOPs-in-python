
#--------------------------------------@property--decorator----------------------------

class Student:

    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage  =str((self.phy + self.chem + self.maths) / 3) + "%"


stu1 = Student(98,97,89)
print(stu1.percentage)

""""this method gives me result as correct but what if I want to change the marks then problem is
I have to change explicilty so to overcome this problem we will use @property method decorator
"""
class Student:

    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
            
        return str((self.phy + self.chem + self.maths) / 3) + "%"


stu1 = Student(98,97,89)


print(stu1.percentage)

stu1.phy= 80

print(stu1.percentage)
