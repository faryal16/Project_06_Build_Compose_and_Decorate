# 15. Method Resolution Order (MRO) and Diamond Inheritance Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.
# 15. Method Resolution Order (MRO) and Diamond Inheritance


def run():
    class A:
        def show(self):
            print("Show from Class A")

    class B(A):
        def show(self):
            print("\n[INFO] Method Called: Show from Class B")

    class C(A):
        def show(self):
            print("[INFO] Method Called: Show from Class C")

    class D(B, C):  # Inherits from B and C
        pass

    # Create object of class D
    d = D()

    print("="*50)
    print("         METHOD RESOLUTION ORDER (MRO) TEST")
    print("="*50)

    # Call the show method from D
    print("\nCalling d.show():")
    d.show()  # This shows which class's 'show' method is called (based on MRO)

    # Print the Method Resolution Order
    print("\nMethod Resolution Order (MRO) for class D:")
    for cls in D.__mro__:
        print(f" - {cls.__name__}")

    print("="*50)



# call the main function
if __name__ == "__main__":
    run() 