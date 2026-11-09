
from calculator import add, sub, mult, div, modul
import os

while True:

    print("==============================")
    print("      SIMPLE CALCULATOR")
    print("==============================")

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Clear")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "6":
        print("Goodbye!")
        break

    elif choice == "5":
        os.system("cls")  
        print("Calculator cleared!")

    elif choice in ["1", "2", "3", "4"]:

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue


        if choice == "1":
            print("Result:", add(a, b))

        elif choice == "2":
            print("Result:", sub(a, b))

        elif choice == "3":
            print("Result:", mult(a, b))

        elif choice == "4":
            try:
                print("Result:", div(a, b))
            except ValueError as error:
                print("Error:", error)

    else:
        print("Invalid choice! Please select 1-6.")

    print()
