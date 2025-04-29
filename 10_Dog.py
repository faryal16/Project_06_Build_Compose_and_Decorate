# 10. Instance Methods Assignment:
# Create a class Dog with instance variables name and breed.
# Add an instance method bark() that prints a message including the dog's name.

def run():
    class Dog:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def bark(self):
            print(f"\n\033[3;34m{self.name}\033[0m, the \033[3;35m{self.breed}\033[0m, says: \033[1;3;33mWoof! Woof!\033[0m")

    # Example usage
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Rocky", "German Shepherd")

    dog1.bark()
    dog2.bark()



# call the main function
if __name__ == "__main__":
    run() 