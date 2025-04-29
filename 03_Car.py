# 3. Public Variables and Methods Assignment:
# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class.


def run():   
    class Car:
        
        
        def __init__(self, brand):
            self.brand = brand

        def start(self):
            print(f"\n{self.brand} car is starting..")
            
    # Create object        
    my_car = Car("Toyota")


    # Public variable access
    print(f"\nCar Brand: {my_car.brand}")

    # pubblic methond call
    my_car.start()

if __name__ == "__main__":
    run() 