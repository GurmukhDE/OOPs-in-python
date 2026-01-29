from loguru import logger

"""below is the example of class inheritance wherein 
Car is the parent class from this 
FordCar which is child class is inheriting from parent
calss"""

class Car:#parent class
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
