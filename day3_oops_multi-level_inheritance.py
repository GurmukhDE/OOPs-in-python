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
