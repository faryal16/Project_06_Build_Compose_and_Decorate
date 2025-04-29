# 🐍 Python OOP Assignments Menu

This is a terminal-based Python application that lets you explore and run multiple **Object-Oriented Programming (OOP)** assignments by choosing from a numbered menu. Each assignment is implemented as a separate Python module and accessed dynamically using Python's `importlib`.

---

## 📂 Project Structure
```bash
06_Build_OOP_Practice_Series/
│
├── main.py               # Main menu interface
├── 01_Student.py         # Assignment 1: Using self
├── 02_Counter.py         # Assignment 2: Using cls
├── 03_Car.py             # Assignment 3: Public variables
├── 04_Bank.py            # Assignment 4: Class variables
├── 05_MathUtils.py       # Assignment 5: Static variables
├── 06_Logger.py          # Assignment 6: Constructor & Destructor
├── 07_Employee.py        # Assignment 7: Access Modifiers
├── 08_Person.py          # Assignment 8: super() function
├── 09_Shape.py           # Assignment 9: Abstract classes
├── 10_Dog.py             # Assignment 10: Instance methods
├── 11_Book.py            # Assignment 11: Class methods
├── 12_TemperatureConverter.py # Assignment 12: Static methods
├── 13_Engine.py          # Assignment 13: Composition
├── 14_Department.py      # Assignment 14: Aggregation
├── 15_Abcd.py            # Assignment 15: Method Resolution Order (MRO)
├── 16_Say_hello.py       # Assignment 16: Function decorators
├── 17_Greet.py           # Assignment 17: Class decorators
├── 18_Product.py         # Assignment 18: Property decorators
├── 19_Multiplier.py      # Assignment 19: callable() and __call__()
├── 20_nvalidAgeError.py  # Assignment 20: Custom exceptions
├── 21_Countdown.py       # Assignment 21: Custom class iterable
```

---

### ▶️ How to Run
Clone or Download the project folder 06_Build_OOP_Practice_Series.

Make sure you have Python 3.8+ installed.

Open your terminal or command prompt, then navigate to the project directory:

```bash

cd path/to/06_Build_OOP_Practice_Series
```
Run the main menu script:

```bash

python main.py
```

You’ll see a menu like this:


### 📚 Python OOP Assignments Menu
1. Using self
2. Using cls
...
21. Custom class iterable
0. Exit
Enter a number to run the corresponding assignment. Each assignment module must contain a run() function.


### 🛠 How It Works
Each assignment must define a run() function that executes its logic.

The main.py uses importlib to dynamically import the selected module.

The assignments dictionary maps menu numbers to both a title and the corresponding Python file name (without .py extension).

✅ Adding a New Assignment
Create a new file, e.g., 22_MyAssignment.py.

Define a run() function inside it.

Add an entry to the assignments dictionary in main.py:

"22": ("My Custom Assignment", "22_MyAssignment"),
### ⚠️ Notes
Module names must follow valid Python naming conventions. Use underscores (_) instead of dots (.) or spaces.

The run() function is mandatory in every assignment file.

### 👨‍🏫 Credits
This project is part of Quarter 3 OOP practice series inspired by Sir Zia's and Sir Asharib Ali's assignments at PIAIC.

### 📃 License
This project is shared for educational purposes. Feel free to fork and expand it.










