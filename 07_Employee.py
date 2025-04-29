# 7. Access Modifiers: Public, Private, and Protected Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

def run():
    class Employee:
        def __init__(self, name, salary, ssn):
            self.name = name
            self._salary = salary #protected
            self.__ssn = ssn #private (name mangled)
            
            
        def show_details(self):
            print(f"\nName: {self.name}")
            print(f"Salary: {self._salary}")
            print(f"SSN (Inside Class): {self.__ssn}")

    # create object
    emp = Employee("Nooru", 80000, "123-45-6789")

    # access public variable
    print("\n✅ Public Variable Access:")
    print("Name:", emp.name)

    # access protected variable
    print("\n✅ Protected Variable Access (Allowed but discouraged):")
    print("Salary:", emp._salary)

    # access private variable
    print("\n❌ Attempt to Access Private Variable:")
    try:
        print("SSN:", emp.__ssn)  # This will raise an AttributeError
    except AttributeError as e:
        print("Error:", e)


    # Correct way to access private variable (not recommended outside class)
    print("\n✅ Accessing Private Variable via Name Mangling:")
    print("SSN (using _Employee__ssn):", emp._Employee__ssn)

    # Showing all details from inside the class
    print("\n📋 Accessing all from a class method:")
    emp.show_details()
    

# call the main function
if __name__ == "__main__":
    run() 