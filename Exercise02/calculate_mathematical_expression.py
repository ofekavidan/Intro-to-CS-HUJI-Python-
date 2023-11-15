#############################################################
# FILE : calculate_mathematical_expression.py
# EXERCISE : intro2cse exercise2 2021
# DESCRIPTION: This function gets two numbers and an operation and returns the result
#############################################################

def calculate_mathematical_expression(num1, num2, operation):
    """This function gets two numbers and an operation and returns the result"""

    if (operation == ":" and num2 == 0):
        return None # Because we can't divide a number by 0

    if operation == "-":
        return float(num1 - num2)
    elif operation == ":":
        return float(num1 /num2)
    elif operation == "+":
        return float(num1 + num2)
    elif operation == "*":
        return float(num1*num2)

    return None # If none of the operations were legal

def calculate_from_string(math_string):
    """This function gets math string (e.g 2 + 2), uses another function and returns the result"""

    num1, operation, num2 = str(math_string).split() # Uses split to exploit the numbers and the operation
    return calculate_mathematical_expression(float(num1),float(num2),operation)

