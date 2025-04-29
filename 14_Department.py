# 14. Aggregation Assignment:
# Create a class Department and a class Employee.
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# ANSI escape sequences for bold and color
BOLD = '\033[1m'
RESET = '\033[0m'
BLUE = '\033[94m'
GREEN = '\033[92m'

def run():
    # Employee class
    class Employee:
        def __init__(self, name, emp_id):
            self.name = name
            self.emp_id = emp_id

        def display_info(self):
            print(f"Employee Name: {BOLD}{GREEN}{self.name}{RESET}")
            print(f"Employee ID: {BOLD}{GREEN}{self.emp_id}{RESET}")


    # Department class (uses aggregation)
    class Department:
        def __init__(self, dept_name, employee):
            self.dept_name = dept_name
            self.employee = employee  # Aggregation: storing a reference

        def show_department_details(self):
            print(f"\nDepartment Name: {BOLD}{BLUE}{self.dept_name}{RESET}")
            self.employee.display_info()


    # Create an Employee object independently
    emp1 = Employee("Alice", 101)

    # Create a Department object and pass the employee
    dept1 = Department("Human Resources", emp1)

    # Display the department and employee details
    dept1.show_department_details()

    # Delete department, employee still exists
    del dept1

    # Show employee still exists
    print(f"\n{BOLD}After deleting department:{RESET}")
    emp1.display_info()


# call the main function
if __name__ == "__main__":
    run() 