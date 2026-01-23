class Divider:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"


d = Divider()
print(d.divide(10, 0))
