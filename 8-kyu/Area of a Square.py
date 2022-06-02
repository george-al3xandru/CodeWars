# Task
# Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. 
# Return the result rounded to two decimals.

import math

def square_area(A):
    r = float((4*A) / (2 * math.pi))
    square_area = round(r*r, 2)
    return square_area
