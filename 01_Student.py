# 1. Using self Assignment:
# Create a class Student with attributes name and marks.
# Use the self keyword to initialize these values via a constructor.
# Add a method display() that prints student details.

def run():
    class Student:
        def __init__(self,name, marks):
            self.name = name
            self.marks = marks
            
        def display(self):
            print(f"\nStudent Name: \033[1;3;36m{self.name}\033[0m")
            print(f"\n{self.name}' Marks: \033[33m{self.marks}\033[0m")

    student1 = Student("Faryal" , 90)
    student1.display()

    student2 = Student("Kulsoom" , 95)
    student2.display()
    
if __name__ == "__main__":
    run()    