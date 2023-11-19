#############################################################
# FILE : car.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise9 2021
# HELPED BY: Annaelle Bensimon
#############################################################

class Car:
    """
    This class represents a car-type object.
    Each car has a length, orientation (0 for vertical and 1 for horizontal), name (color), and position on the board.
    To avoid errors, I set the initial value of each car to the following values:
    length 2, orientation 0, name Y (yellow), and position on the board 0,0.

    In addition, I chose to make these variables private
    """



    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """

        self.__name = name
        self.__location = location
        self.__length = length
        self.__orientation = orientation


    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        lst = []
        lst.append(self.__location)

        counter = 1
        a, b = self.__location
        while len(lst) != self.__length:
            if self.__orientation == 1:
                lst.append((a, b + counter))
            if self.__orientation == 0:
                lst.append((a + counter, b))
            counter+= 1

        return lst


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """

        dict = {}
        # a, b = self.__location
        #
        # if self.__orientation == 0:
        #     if a != 0:
        #         dict['u'] = "cause the car to move up"
        #     if a != 6:
        #         dict['d'] = "cause the car to move down"
        #
        # if self.__orientation == 1:
        #     if b != 0:
        #         dict['l'] = "cause the car to move left"
        #     if b != 6:
        #         dict['r'] = "cause the car to move right"

        if self.__orientation == 0:
            dict['u'] = "cause the car to move up"
            dict['d'] = "cause the car to move down"

        if self.__orientation == 1:
            dict['l'] = "cause the car to move left"
            dict['r'] = "cause the car to move right"


        return dict


    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """

        lst_coordinates = self.car_coordinates()
        lst_cells_to_be_empty = []

        if movekey == "r" and self.__orientation == 1:
            a_temp, b_temp = lst_coordinates[-1]
            lst_cells_to_be_empty.append((a_temp, b_temp + 1))

        if movekey == "l" and self.__orientation == 1:
            a_temp, b_temp = lst_coordinates[0]
            lst_cells_to_be_empty.append((a_temp, b_temp - 1))

        if movekey == "u" and self.__orientation == 0:
            a_temp, b_temp = lst_coordinates[0]
            lst_cells_to_be_empty.append((a_temp - 1, b_temp))

        if movekey == "d" and self.__orientation == 0:
            a_temp, b_temp = lst_coordinates[-1]
            lst_cells_to_be_empty.append((a_temp + 1, b_temp))

        return lst_cells_to_be_empty



    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey in self.possible_moves():

            a, b = self.__location

            if movekey == "r":
                b = b + 1
            if movekey == "l":
                b = b - 1
            if movekey == "u":
                a = a - 1
            if movekey == "d":
                a = a + 1

            self.__location = a, b

            return True

        return False




    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name

