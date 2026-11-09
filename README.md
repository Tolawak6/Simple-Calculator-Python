# Simple Command-Line Calculator

A beginner-friendly command-line calculator built with Python. This project demonstrates fundamental programming concepts, including functions, conditional statements, loops, exception handling, modular programming, and automated testing.

## Features

- **Addition (+):** Adds two numbers.
- **Subtraction (-):** Subtracts one number from another.
- **Multiplication (*):** Multiplies two numbers.
- **Division (/):** Divides two numbers with division-by-zero protection.
- **Clear:** Clears the terminal screen.
- **Exit:** Safely terminates the application.
- **Input Validation:** Handles invalid menu selections and non-numeric inputs.
- **Automated Testing:** Uses Python's built-in `unittest` framework.

## Technologies Used

- Python 3
- Visual Studio Code
- Python `unittest` module
- Python `os` module

## Project Structure

```text
simple-calculator/
│
├── main.py              # Main application and interactive menu
├── calculator.py        # Arithmetic calculation functions
├── test_calculator.py   # Automated unit tests
└── README.md            # Project documentation
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd simple-calculator
```

### 3. Run the application

```bash
python main.py
```

## How to Use

After starting the application, the following menu will appear:

```text
================================
       SIMPLE CALCULATOR
================================

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Clear
6. Exit

Choose an option:
```

1. Select an arithmetic operation.
2. Enter the first number.
3. Enter the second number.
4. View the calculation result.
5. Continue calculating or select Exit to close the application.

## Running Automated Tests

The project includes automated unit tests to verify the calculation functions.

Run the following command from the project directory:

```bash
python -m unittest -v
```

The tests cover:

- Addition
- Subtraction
- Multiplication
- Division
- Decimal calculations
- Negative numbers
- Division by zero

## Error Handling

The application handles common errors, including:

- Invalid menu selections.
- Non-numeric input.
- Division by zero.

These validations help prevent unexpected application crashes.

## Learning Objectives

This project was developed as part of an internship programming assignment to practice:

- Writing and calling Python functions.
- Using conditional statements and loops.
- Handling exceptions with `try` and `except`.
- Organizing code into separate modules.
- Validating user input.
- Writing automated unit tests.

## Future Improvements

- Add modulo (%) and exponentiation operations.
- Support calculation history.
- Allow users to perform multiple operations in one expression.
- Improve the command-line interface.

## Author

**Tolawak Merga**

GitHub: [@Tolawak6](https://github.com/Tolawak6)

---

*Developed as a Python internship project.*