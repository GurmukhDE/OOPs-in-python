class CarInventory:
    def __init__(self, cars):
        self.cars = cars   # list of dicts

    def print_all_cars(self):
        for car in self.cars:
            print(car["brand"], car["model"], car["country"])


cars_data = [
    {"brand": "Ford", "model": "Bronco", "country": "USA"},
    {"brand": "BMW", "model": "X5", "country": "Germany"},
    {"brand": "Tata", "model": "Safari", "country": "India"}
]

inventory = CarInventory(cars_data)
inventory.print_all_cars()
