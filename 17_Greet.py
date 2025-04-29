# 7. Class Decorators Assignment:
# Create a class decorator add_greeting that modifies 
# a class to add a greet() method returning "Hello from Decorator!".
# Apply it to a class Person.


def run():
    def add_greeting(cls):
        """
        This decorates adds a greet() method to the class
        """
        
        def greet():
            return "\n👋 Hello from Decorator!"
        
        
        # add the greet method to class
        cls.greet = greet
        return cls

    # applying the decorator to a class
    @add_greeting
    class Person:
        def __init__(self, name):
            self.name = name
            
        def say_name(self):
            return f"\nMy name is \033[1;3;35m{self.name}\033[0m."
        
        
    # Create an instance of Person
    person = Person("Faryal")

    # call the greet()mathod
    print(person.greet())

    # Call other method
    print(person.say_name())
    

# call the main function
if __name__ == "__main__":
    run() 