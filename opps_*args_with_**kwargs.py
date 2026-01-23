class Calculator:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        return total


calc = Calculator()
print(calc.add(10, 20, 30))
