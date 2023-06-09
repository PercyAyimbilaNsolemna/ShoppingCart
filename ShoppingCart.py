import random

class ShoppingCart:
    def __init__(self, items=None, total_price=0, prices=None):
        self.items = []
        self.total_price = total_price
        self.prices = [10, 20, 30, 40, 50]

    #Creates an __str__ method that makes it possible to pass an object created from this class to the print function
    def __str__(self):
        return "This is Shooping Cart class"
    
    #Creates a method that makes the user add a number of items
    def add_item(self, *item):
        self.item = item
        for an_item in self.item:
            self.items.append(an_item)
        for _ in self.items:
            price = random.choice(self.prices)
            self.total_price = self.total_price + price

    #Creates a method that removes elements
    def remove_item(self, *item):
        self.item = item
        for an_item in self.item:
            if an_item in self.items:
                self.items.remove(an_item)
                self.total_price = self.total_price - random.choice(self.prices)


    #Creates a getter and setter for item
    def get_item(self):
        return self.add_item
    

    def set_item(self, item):
        self.item = item


    #Creates a getter and setter for total price 
    def get_total_price(self):
        return self.total_price
    
    #Creates a setter for the total_price
    def set_total_price(self, total_price):
        self._total_price = total_price

    #Creates a getter and setter using python's property approach
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, items):
        self._items = items


def main():

    shoppingCart = ShoppingCart()

    shoppingCart.add_item("Banana")

    print(shoppingCart.total_price)

    shoppingCart.add_item("Mango", "Guava")

    print(shoppingCart.items)

    shoppingCart.add_item("Orange")

    print(shoppingCart.items)

    print(shoppingCart.total_price)

    shoppingCart.remove_item("Orange")
    print(shoppingCart.items)

    print(shoppingCart.total_price)

    shoppingCart.remove_item("Orange", "Mango")
    print(shoppingCart.items)

    print(shoppingCart.total_price)

    shoppingCart.remove_item("Orange", "Mango", "Rice")
    print(shoppingCart.items)


if __name__ == "__main__":
    main()
    
