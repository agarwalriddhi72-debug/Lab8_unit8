"""
Program name: Geometry calculator
Name: Riddhi Agarwal
Purpose of program: To calculate area and perimeter of a circle and a rectangle
Starter code: None
Date: March 2, 2026
"""

from circle import circumference
from rectangle import perimeter
from circle import area as a1
from rectangle import area as a2

#Both circle and rectangle have a function named "area" and a function names "perimeter."
#So aliases are necessary to avoid name conflict.
#Without aliases, Python wouldn't know which "area" function to call
#We can avoid name conflict by calling the function after the module name

#Function to check if the number is valid; Check if it's not negative, it doesn't have text or more than one decimal point
def pos_value(number):
    decimal_count = 0

    for char in number:
        if char == ".":
            decimal_count += 1
        elif not char.isdigit():
            print("Please enter a valid number.")
            return False

    if decimal_count > 1:
        print("Please enter a valid number.")
        return False

    if float(number) > 0:
        return True

#Flag variable
active = True

while active:
    program_name = "Geometry Calculator"
    print(program_name.center(50))
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")

    choice = input("Please enter your choice (1-5): ")

    #First choice
    if choice == "1":
        #Check if the number is positive
        while True:
            radius = input("Enter the radius of the circle: ")
            
            if pos_value(radius):
                radius = float(radius)
                break
        result = a1(radius)
        print(f"The area of the circle is {round(result, 3)}")

    #Second choice
    elif choice == "2":
        #Check if the number is positive
        while True:
            radius = input("Enter the radius of the circle: ")

            if pos_value(radius):
                radius = float(radius)
                break
        result = circumference(radius)
        print(f"The circumference of the circle is {round(result, 3)}")

    #Third choice
    elif choice == "3":
        #Check if the numbers are positive
        while True:
            width = input("Enter the width of the rectangle: ")
            if pos_value(width):
                width = float(width)
                break
        while True:
            height = input("Enter the height of the rectangle: ")
            if pos_value(height):
                height = float(height)
                break

        result = a2(width, height)
        print(f"The area of the rectangle is {round(result, 3)}")

    #fourth choice
    elif choice == "4":
        #Check if the numbers are positive
        while True:
            width = input("Enter the width of the rectangle: ")
            if pos_value(width):
                width = float(width)
                break
        while True:
            height = input("Enter the height of the rectangle: ")
            if pos_value(height):
                height = float(height)
                break

        result = perimeter(width, height)
        print(f"The perimeter of the rectangle is {round(result, 3)}")

    #fifth choice
    else:
        print("Goodbye!")
        break