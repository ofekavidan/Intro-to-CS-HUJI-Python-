#############################################################
# FILE : quadratic_equation.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise2 2021
# DESCRIPTION: This function gets 3 coefficients and returns the solutions of the quadratic equation
#############################################################

import math

# I got help by w3resource.com

def quadratic_equation(a, b, c):
    """This function gets 3 coefficients and returns the solutions of the quadratic equation"""
    root_value = b*b - (4*a*c)

    first_solution = None # Initial boot
    second_solution = None # Initial boot

    if root_value > 0: # Two solutions
        first_solution = (((-b) + math.sqrt(root_value))/(2*a))
        second_solution =(((-b) - math.sqrt(root_value))/(2*a))

    if root_value == 0: # One solution
        first_solution = (-b) / 2 / a

    return first_solution, second_solution

def quadratic_equation_user_input():
    """This function asking the user for quadratic equation (string)
    and split it to 3 coefficients (a, b, c)
    it also uses the upper function to get the solutions for the equation"""

    equation_string = input("Insert coefficients a, b, and c: ")
    a, b, c = equation_string.split()
    if(a == "0"):
        print("The parameter 'a' may not equal 0")
    else:
        first_solution, second_solution = quadratic_equation(float(a),float(b),float(c))
        if(first_solution == None):
            if second_solution == None:
                print("The equation has no solutions")

        elif second_solution == None:
            print("The equation has 1 solution: " + str(first_solution))
        else:
            print("The equation has 2 solutions: " + str(first_solution) + " and " + str(second_solution))





