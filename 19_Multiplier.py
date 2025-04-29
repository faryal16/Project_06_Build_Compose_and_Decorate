# 19. callable() and __call__() Assignment:
# Create a class Multiplier with an __init__() to set a factor.
# Define a __call__() method that multiplies an input by the factor.
# Test it with callable() and by calling the object like a function.

def run():
    class Multiplier:
        def __init__(self, factor):
            self.factor = factor

        def __call__(self, value):
            result = value * self.factor
            print(f"\n[CALL] Multiplying {value} by factor {self.factor} = {result}")
            return result

    # Create a multiplier object
    times_three = Multiplier(3)

    # Check if the object is callable
    print("\nIs 'times_three' callable?", callable(times_three))  # True

    # Use the object like a function
    result = times_three(10)  # Calls __call__(10)

    # Optional: Print the result
    print("\nResult:", result)


# call the main function
if __name__ == "__main__":
    run() 