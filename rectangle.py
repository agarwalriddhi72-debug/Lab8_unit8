"""
Program name: Geometry calculator - Rectangle Module
Name: Riddhi Agarwal
Date: March 3, 2026
Starter code: None

Purpose of program: 
To calculate area and perimeter of a rectangle.

Functions:
- area(width, height): Returns the area of the rectangle.
- perimeter(width, height): Returns the perimeter of the rectangle.
"""

import math

def area(width, height):
    """
    Calculates the area of a rectangle
    Parameters:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    Returns:
        float: The area of the rectangle
    """
    return width * height

def perimeter(width, height):
    """
    Calculates the perimeter of the rectangle
    Parameters:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    Returns:
        float: The perimeter of the rectangle
    """
    return 2*width + 2*height