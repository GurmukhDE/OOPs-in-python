class Car:
    brand = "Ford"
    model = "bronco"

car1 = Car

print(car1.brand, car1.model)


class Student:
    def __init__(self, fullname):
        self.name = fullname


s1= Student("gurmukh")

print(s1.name)


class Car:
    def __init__(self, brand,model, country):
        self.brand = brand
        self.model = model
        self.country = country

car_info = Car("Ford", "Bronco", "USA")
print(car_info.brand, car_info.model, car_info.country)





