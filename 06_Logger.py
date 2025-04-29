# 6. Constructors and Destructors Assignment:
# Create a class Logger that prints a message when 
# an object is created (constructor) and another message 
# when it is destroyed (destructor).


def run():
    class Logger:
        
        # Constructor
        def __init__(self):
            print("\nLogger object has been created!")
            
        # Destructor
        def __del__(self):
            print("\nLogger object has been destroyed!")
            
    # creat object
    logger1 = Logger()

    # delete the object
    del logger1
    

# call the main function
if __name__ == "__main__":
    run() 