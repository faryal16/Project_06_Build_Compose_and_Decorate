# 18. Property Decorators: @property, @setter, and @deleter Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


def run():
    class Product:
        def __init__(self, price):
            self.price = price
            
        @property
        def price(self):
            """
            Getter method for _price
            """
            print("\n📝  [GET] Getting price...")
            return self._price
        
        @price.setter
        def price(self, value):
            """
            Setter method for _price
            """
            if value < 0:
                print("\n❌ [SET] Price can't be negative!")
            else:
                print(f"\n✅  [SET] Setting price to {value}")
                self._price = value

        @price.deleter
        def price(self):
            """
            Deleter method for _price
            """
            print("\n🚮 [DELETE] Deleting price...")
            del self._price

        
    # Testing the Product class
    p = Product(100)

    # get the price
    print("\nPrice: ", p.price)


    # Set a new price
    p.price = 150  # Calls the setter


    # Try setting a negative price
    p.price = -50

    # Delete the price
    del p.price # Calls the deleter

    try:
        print("\nPrice: ", p.price)
    except AttributeError:
        print("\n⚠️  Price attribute has been deleted!")
        

# call the main function
if __name__ == "__main__":
    run() 