from ShoppingCart import ShoppingCart

def main():
    #Creates an object from the ShoppingCart class
    shoppingCart = ShoppingCart()

    #Passes the shoppingCart object to the print function
    print(shoppingCart)

    #Adds an item to the ShoppingCart using the add_item method and prints the total price
    shoppingCart.add_item("Banana")
    print(shoppingCart.total_price)

    #Adds two items to the ShoppingCart using the add_item method and outputs the total_price
    shoppingCart.add_item("Mango", "Guava")
    shoppingCart.add_item("Orange")
    print(shoppingCart.items)
    print(shoppingCart.total_price)

    #Revomes one item from the items using the remove_item method
    shoppingCart.remove_item("Orange")
    print(shoppingCart.items)
    print(shoppingCart.total_price)

    #Removes two items from the items using the remove_item method
    shoppingCart.remove_item("Orange", "Mango")
    print(shoppingCart.items)
    print(shoppingCart.total_price)

    #Removes three items that are not in the list 
    shoppingCart.remove_item("Orange", "Mango", "Rice")
    print(shoppingCart.items)


if __name__ == "__main__":
    main()