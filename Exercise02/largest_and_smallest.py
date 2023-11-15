#############################################################
# FILE : largest_and_smallest.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise2 2021
# DESCRIPTION: This function gets 3 numbers and returns the largest and the smallest
#############################################################

def largest_and_smallest(num1, num2, num3):
    """This function gets 3 numbers and returns the largest and the smallest"""
    large = num1 # Initial boot
    small = num1 # Initial boot

    if(num1 >= num2):
        if(num1 >= num3):
            large = num1
            if (num2 > num3):
                small = num3
            else:
                small = num2
        else:
            large = num3
            small = num2
    elif (num2 >= num3):
        large = num2
        if (num1 >= num3):
            small = num3
        else:
            small = num1
    else:
        large = num3


    return large, small

def check_largest_and_smallest():
    """This function checks if the other function works well

    I chose 1, 1.0, -7 because it combines two identical numbers
    one of them with decimal point, and the other without decimal point

    I chose -10, -23.5, -3 because it combines three negative numbers
    one of them with decimal point
    """
    its_work = True # Initial boot

    large, small = largest_and_smallest(17,1,6)
    if (large != 17 or small != 1):
        its_work = False

    large, small = largest_and_smallest(1, 17, 6)
    if (large != 17 or small != 1):
        its_work = False

    large, small = largest_and_smallest(1, 1, 2)
    if (large != 2 or small != 1):
            its_work = False


    # I chose 1, 1.0, -7 because it combines two identical numbers
    # one of them with decimal point, and the other without decimal point
    large, small = largest_and_smallest(1, 1.0, -7)
    if (large != 1 or small != -7):
            its_work = False

    # I chose -10, -23.5, -3 because it combines three negative numbers
    # one of them with decimal point

    large, small = largest_and_smallest(-10, -23.5, -3)
    if (large != -3 or small != -23.5):
            its_work = False

    return its_work

