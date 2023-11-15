#############################################################
# FILE : temperature.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise2 2021
# DESCRIPTION: This function gets three temperatures of three different days
#     it gets a threshold temperature as well
#     it returns True if two of the days (or more) have higher temperature than the threshold
#############################################################

def is_it_summer_yet(temp, day1, day2, day3):
    """This function gets three temperatures of three different days
    it gets a threshold temperature as well
    it returns True if two of the days (or more) have higher temperature than the threshold"""
    counter = 0 # a variant which will count the number of days that have higher temperature than the threshold
    if (day1 > temp):
        counter = counter + 1
    if (day2 > temp):
        counter = counter + 1
    if (day3 > temp):
        counter = counter + 1

    return (counter > 1)

