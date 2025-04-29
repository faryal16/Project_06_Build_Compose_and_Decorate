import sys
import importlib

assignments = {
    "1": ("Using self", "01_Student"),
    "2": ("Using cls", "02.Counter"),
    "3": ("Using Public Variables", "03_Car"),
    "4": ("Using Class Variables", "04_Bank"),
    "5": ("Using Static Variables", "05_MathUtils"),
    "6": ("Using Constructors and Destructors", "06_Logger"),
    "7": ("Using Access Modifiers", "07_Employee"),
    "8": ("Using super() Function", "08_Person"),
    "9": ("Using Abstract Classes", "09_Shape"),
    "10": ("Using Instance Methods", "10_Dog"),
    "11": ("Using Class Methods", "11_Book"),
    "12": ("Using Static Methods", "12_TemperatureConverter"),
    "13": ("Using Composition", "13_Engine"),
    "14": ("Using Aggregation", "14_Department"),
    "15": ("Using Method Resolution Order (MRO)", "15_Abcd"),
    "16": ("Using Function Decorators", "16_Say_hello"),
    "17": ("Using Class Decorators", "17_Greet"),
    "18": ("Using Property Decorators", "18_Product"),
    "19": ("Using callable() and __call__()", "19_Multiplier"),
    "20": ("Using Custom Exception", "20_nvalidAgeError"),
    "21": ("Using Custom Class Iterable", "21_Countdown"),
}

def main():
    while True:
        print("\n📚 Python OOP Assignments Menu")
        for key, (title, _) in assignments.items():
            print(f"{key}. \033[1;3;35m{title}\033[0m")
        print("0. Exit")

        choice = input("\nChoose an assignment to run (0 to exit): ")

        if choice == "0":
            print("\n👋 Exiting. Goodbye!")
            sys.exit()
        elif choice in assignments:
            # Dynamically import the module using importlib
            module_name = assignments[choice][1]
            try:
                module = importlib.import_module(module_name)
                print("="*50)
                print(f"\n🧠 Running: \033[1;3;36m{assignments[choice][0]}\033[0m\n")
                module.run()  # Assuming all assignments have a run() method
                print("="*50)
            except ModuleNotFoundError:
                print("="*50)
                print(f"\n❌ Error: Could not find the module '{module_name}'.")
                print("="*50)
        else:
            print("\n❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
