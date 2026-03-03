"""
Program name: Geometry calculator - Circle Module
Name: Riddhi Agarwal
Date: March 3, 2026
Starter code: None

Purpose of program: 
To calculate area and perimeter of a circle.

Functions:
- area(radius): Returns the area of a circle given the radius
- circumference(radius): Returns the circumference of a circle given the radius
"""

import math

def area(radius):
    """
    Calculates the area of a circle.
    Parameters:
        radius (float): The readius of the circle
    Returns: float: The are of the circle
    """
    return math.pi * (radius ** 2)

def circumference(radius): 
    """
    Calculates the circumference of a circle.
    Parameters:
        radius (float): The radius of the circle.
    Returns:
        float: The circumference of the circle
    """
    return 2 * math.pi * radius