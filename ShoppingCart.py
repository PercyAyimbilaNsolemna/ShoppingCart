
class ShoppingCart:
    def __init__(self, items=None, total_price=None):
        self.items = []
        self.total_price = total_price

    #Creates an __str__ method that makes it possible to pass an object created from this class to the print function
    def __str__(self):
        return "This is Shooping Cart class"
    
