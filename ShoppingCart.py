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
        items = []
        items.append(item)
        self.items = items
        prices = [10, 20, 30, 40, 50]
        for _ in self.items:
            price = random.choice(prices)
            self.total_price = self.total_price + price

    #Creates a method that removes elements
    def remove_item(self, *item):
        for item in self.items:
            self.items.pop(item)

    #Creates a getter and setter for item
    def set_item(self, item):
        self.item = item
def main():

    shoppingCart = ShoppingCart()

    shoppingCart.add_item("Banana")

    print(shoppingCart.total_price)

    shoppingCart.add_item("Mango")

    print(shoppingCart.total_price)

    shoppingCart.add_item("Orange", "Apple")

    print(shoppingCart.total_price)


if __name__ == "__main__":
    main()
    
