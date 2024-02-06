# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
        
    BEWARE: there may be a bug or two in this code
    """

    # Input validation: values should be > 0 and <= 200
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Verify that all 3 inputs are integers
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Triangle inequality check
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        return 'NotATriangle'

    # Classification of triangle
    if a == b and b == c:
        return 'Equilateral'
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return 'Right'
    elif a != b and b != c and a != c:
        return 'Scalene'
    else:
        return 'Isosceles'

if __name__ == "__main__":
    # examples of running the code
    print(classifyTriangle(1, 2, 3))  # Expected: NotATriangle
    print(classifyTriangle(1, 1, 1))  # Expected: Equilateral
    print(classifyTriangle(3, 4, 5))  # Expected: Right
