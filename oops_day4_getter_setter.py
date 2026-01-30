class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def show_total(cls):
        print(cls.total_cars)
#-----------------------------------------------

class Labour:
    def __init__(self, wage):
        self.__wage = wage

    def get_wage(self):
        return self.__wage

    def set_wage(self, wage):
        if wage > 0:
            self.__wage = wage
          
#-----------------------------------------------------------


