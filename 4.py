from collections import namedtuple

Car = namedtuple('Car', ['marka', 'model', 'year'])

class Car1:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def info(self):
        print(f"Model: {self.model}, Color: {self.color}, Year: {self.year}, Price: {self.price}")

car1 = Car1('Mercedes', 'Black', 2014, 50000)
car1.info(1)
