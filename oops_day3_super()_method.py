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


