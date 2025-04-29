# 2. Using cls Assignment:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

def run():
        
    class Counter:
        object_count = 0
        
        def __init__(self):
            Counter.object_count += 1
            print(f"\nObject {Counter.object_count} created.")
            
        @classmethod
        def display_count(cls):
            print(f"\nTotal {cls.object_count} objects created.")
            
    # Create objects    
    obi1 = Counter()
    obi2 = Counter()
    obi3 = Counter()

    # Class method Called
    Counter.display_count()
    
if __name__ == "__main__":
    run()        