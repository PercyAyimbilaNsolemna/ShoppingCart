from ShoppingCart import ShoppingCart

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