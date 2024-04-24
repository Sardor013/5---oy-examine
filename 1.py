from decimal import Decimal

class ToDecimal:
    def __init__(self, number):
        self.decimal = Decimal(str(number))

son = int(input("-->"))
num = ToDecimal(son)
print(num.decimal)
