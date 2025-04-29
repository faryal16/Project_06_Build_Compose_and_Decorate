# 21. Make a Custom Class Iterable Assignment:
# Create a class Countdown that takes a start number.
# Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

def run():
    class Countdown:
        def __init__(self, start):
            self.start = start

        def __iter__(self):
            self.current = self.start
            return self

        def __next__(self):
            if self.current < 0:
                raise StopIteration
            else:
                value = self.current
                self.current -= 1
                return value

    # Test the Countdown class
    print("\nCountdown from 5:")
    for num in Countdown(5):
        print(num)



# call the main function
if __name__ == "__main__":
    run() 