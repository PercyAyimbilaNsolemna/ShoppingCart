import random

class ShoppingCart:
    def __init__(self, items=None, total_price=0):
        self.items = []
        self.total_price = total_price

    #Creates an __str__ method that makes it possible to pass an object created from this class to the print function
    def __str__(self):
        return "This is Shooping Cart class"
    
    #Creates a method that makes the user add a number of items
    def add_item(self, *item):
        self.items.append[item]
        prices = [10, 20, 30, 40, 50]
        for item in len(self.items):
            price = random.choice(prices)
            self.total_price = self.total_price + price
    
