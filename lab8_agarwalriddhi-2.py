"""
Program name: Geometry calculator
Name: Riddhi Agarwal
Date: March 3, 2026
Starter code: None

Purpose of program: 
To calculate area and perimeter of a circle and a rectangle.
The user can choose from a menu to calculate:

1. Area of a circle
2. Circumference of a circle
3. Area of a rectangle
4. Perimeter of a rectangle
"""

import circle
import rectangle

#Both circle and rectangle have a function named "area" and a function names "perimeter."
#So aliases are necessary to avoid name conflict.
#Without aliases, Python wouldn't know which "area" function to call
#We can avoid name conflict by calling the function after the module name

def pos_value(number):
    """
    This function validates user input to ensure it is a positive number.

    It checks:
    - If the number contains only digits and at most one decimal point
    - Doesn't contain letters or special characters
    - Is greater than 0

    Parameters:
        number (str): The user input that needs to be validated
    Returns:
        boolean: True if user input is a valid positive number, otherwise False
    """

    decimal_count: int = 0

    for char in number:
        if char == ".":
            decimal_count += 1
        elif not char.isdigit():
            print("Please enter a valid number.")
            return False

    if decimal_count > 1:
        print("Please enter a valid number.")
        return False

    if number == ".":
        print("Please enter a valid number.")
        return False
    
    if float(number) > 0:
        return True
    
    else:
        print("Please enter a number greater than 0.")
        return False

#Controls main program loop
active: bool = True

while active:
    program_name = "Geometry Calculator"
    print(program_name.center(34))
    print("---------------------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")
    print()

    choice: str = input("Please enter your choice (1-5): ")
    print()

    #Option 1: Calculate circle area
    if choice == "1":
        #Validate the radius
        while True:
            radius: str = input("Enter the radius of the circle: ")
            
            if pos_value(radius):
                radius = float(radius)
                break
        result: float = circle.area(radius)
        print(f"The area of the circle is {round(result, 3)}.")
        print()
        input("Press Enter to continue...")

    #Option 2: Calculate Circle Circumference
    elif choice == "2":
        #Validate the radius
        while True:
            radius: str = input("Enter the radius of the circle: ")

            if pos_value(radius):
                radius = float(radius)
                break
        result: float = circle.circumference(radius)
        print(f"The circumference of the circle is {round(result, 3)}")
        print()
        input("Press Enter to continue...")

    #Option 3: Calculate Rectangle Area
    elif choice == "3":
        #Validate the width and height
        while True:
            width: str = input("Enter the width of the rectangle: ")
            if pos_value(width):
                width = float(width)
                break
        while True:
            height: str = input("Enter the height of the rectangle: ")
            if pos_value(height):
                height = float(height)
                break

        result: float = rectangle.area(width, height)
        print(f"The area of the rectangle is {round(result, 3)}")
        print()
        input("Press Enter to continue...")

    #Option 4: Calculate Rectangle Perimeter
    elif choice == "4":
        #Validate the width and height
        while True:
            width: str = input("Enter the width of the rectangle: ")
            if pos_value(width):
                width = float(width)
                break
        while True:
            height: str = input("Enter the height of the rectangle: ")
            if pos_value(height):
                height = float(height)
                break

        result: float = rectangle.perimeter(width, height)
        print(f"The perimeter of the rectangle is {round(result, 3)}")
        print()
        input("Press Enter to continue...")

    #fifth choice
    else:
        print("Goodbye!")
        break

    print()