# 13. Composition Assignment:
# Create a class Engine and a class Car. 
# Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.

def run():
    class Engine:
        def start(self):
            print("\n🔧 Engine is starting... Vroom! 🚗💨")
            
    class Car:
        def __init__(self, engine):
            self.engine = engine # Composition: Engine is a part of Car
            
        def start_car(self):
            print("\n🚘 Starting the car...")
            self.engine.start()  # Accessing Engine method via Car

    # Example usage
    my_engine = Engine()
    my_car = Car(my_engine)

    my_car.start_car()
 

# call the main function
if __name__ == "__main__":
    run()     