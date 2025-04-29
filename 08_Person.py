# 8. The super() Function Assignment:
# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

def run():
    # Base classs
    class Person:
        def __init__(self, name):
            self.name = name
            
    # Derived class
    class Teacher(Person):
        def __init__(self , name , subject):
            super().__init__(name) # call the constructer of Person
            self.subject = subject
        
        def introduce(self):
            print(f"\nMy name is \033[1;3;35m{self.name}\033[0m, and I teach \033[1;3;34m{self.subject}\033[0m")
            
    # create object
    teacher1 = Teacher("Mr.Zia Khan", "Agentic Ai")
    teacher2 = Teacher("Mr.Asharib Ali", "Python")

    teacher1.introduce()
    teacher2.introduce()
            

# call the main function
if __name__ == "__main__":
    run()     