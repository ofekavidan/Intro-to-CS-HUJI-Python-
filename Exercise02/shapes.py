#############################################################
# FILE : shapes.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise2 2021
# DESCRIPTION: This function inputs the type of the shape, and than calculates its area
#############################################################

import math

def calc_circle():
    radius = float(input())
    return ((radius * radius) * math.pi)

def calc_rectangle():
    side1 = float(input())
    side2 = float(input())

    return side1*side2

def calc_triagnle():
    side = float(input())
    return (side * side * math.sqrt(3) / 4)

def shape_area():
    """This function inputs the type of the shape, and than calculates its area"""

    area = 0
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if((shape != "1") and (shape != "2") and (shape != "3")):
        return None

    if shape == "1":
        area = calc_circle()

    if shape == "2":
        area = calc_rectangle()

    if shape == "3":
        area = calc_triagnle()
    return area


