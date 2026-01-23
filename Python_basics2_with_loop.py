class Numbers:
    def __init__(self, nums):
        self.nums = nums

    def print_even(self):
        for n in self.nums:
            if n % 2 == 0:
                print(n)


obj = Numbers([1, 2, 3, 4, 5, 6])
obj.print_even()

#---------------------------------------

class OrderValidator:
    def __init__(self, orders):
        self.orders = orders

    def valid_orders(self):
        valid = []
        for order in self.orders:
            if order["amount"] > 0:
                valid.append(order)
        return valid


orders = [
    {"id": 1, "amount": 200},
    {"id": 2, "amount": -50},
    {"id": 3, "amount": 500}
]

validator = OrderValidator(orders)
print(validator.valid_orders())

