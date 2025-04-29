# 9. Abstract Classes and Methods Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod


def run():
    # Abstract base class
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
        
    #Concreate subclass
    class Reactangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            
        def area(self):
            return self.width * self.height
        
    # creart object
    rect = Reactangle(5,10)
    rect1 = Reactangle(13,15)
    print(f"\nArea of rectangle with width {rect.width} and height {rect.height} is \033[35m{rect.area()}\033[0m")
    print(f"\nArea of rectangle with width {rect.width} and height {rect.height} is \033[35m{rect1.area()}\033[0m")
    

# call the main function
if __name__ == "__main__":
    run() 