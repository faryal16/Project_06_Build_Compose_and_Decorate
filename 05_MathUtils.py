# 5. Static Variables and Static Methods Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.


def run():
    class MathUtils:
        
        @staticmethod
        def add(a,b):
            return a + b
        
    # Test the static method
    result1 = MathUtils.add(5, 10)
    result2 = MathUtils.add(-2, 7)
    result3 = MathUtils.add(3.5, 4.5)
    print("\nThe sum of 5 + 10 =", result1 )
    print("The sum of -2 + 7 =", result2 )
    print("The sum of 3.5 + 4.5 =", result3)
    

# call the main function
if __name__ == "__main__":
    run() 