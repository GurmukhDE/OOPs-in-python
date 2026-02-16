from loguru import logger

"""below is the example of class inheritance wherein 
Car is the parent class from this 
FordCar which is child class is inheriting from parent
calss"""




class Car:#parent class # this is our decorator as private method.
    @staticmethod
    def start():
        return ("car started...")

    @staticmethod
    def stop():
        return ("car stopped...")

class FordCar(Car):#child class
    def __init__(self, name):
        self.name = name


car1 = FordCar("Ecosport")
car2 = FordCar("Bronco")


logger.info(car1.start(),  car2.stop())
"""above is the single inheritance class example"""

"""THERE ARE 3 TYPE OF INHERITANCES
1- Single inheritance
2- multi- leverl inheritance
3- multiple inheritance

"""
#--------------------------------------------------------------------------------------

"""below the example of multi-level inheritance"""

class Car:#parent class
    @staticmethod
    def start():
        return ("car started...")

    @staticmethod
    def stop():
        return ("car stopped...")

class FordCar(Car):#child class
    def __init__(self, brand):
        self.brand = brand


class Ecosport(FordCar):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type



car1 = Ecosport("Diesel")
car1.start()
#---------------------------------------Multiple inheritance----------------------------

"""In multiple inheritance a child class can inherit from 2 parent class see example below"""


class A:
    varA = "welcome to the class A"

class B:
    varB =  "welcome to class B"

class C(A, B):
    varC = "welcome to class C"



c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)

#--------------------------super()method---------------------------------------

"""super()method we used to access method of the parent class"""



class Car:#parent class

    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    @staticmethod
    def start():
        return ("car started...")

    @staticmethod
    def stop():
        return ("car stopped...")

class FordCar(Car):#child class
    def __init__(self, brand):
        self.brand = brand


class Ecosport(FordCar):
    def __init__(self, name, fuel_type):
        super().__init__(fuel_type)
        self.name = name
        super().start()
"""now here I want to access parent class's fuel_type"""

car_new = FordCar("Mustang", "Electric")
print(car_new.fuel_type)      





#---------------------------@classmethod-decorator--------------------------------

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Rahul kuamr")    
print(p1.name)
print(Person.name)



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
