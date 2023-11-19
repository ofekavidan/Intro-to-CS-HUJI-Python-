#############################################################
# FILE : board.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise9 2021
# HELPED BY: Annaelle Bensimon
#############################################################

import copy


class Board:
    """
    This class represents a board-type object.
    Through it we will create the board, and use it for the following:
    We can print it, we can put cars on it, we can move the cars that are on it
    """

    def __init__(self):

        # board_lists = [[' '] * self.width for rows in range(self.height)]
        # From Tirgul 9

        self.__cars = {}

        self.__board = [["_" for _ in range(7)] for _ in range(7)]
        self.__board[3].append("_")

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        string1 = ""
        for i, curr in enumerate(self.__board):
            string1 += ' '.join(self.__board[i]) + '\n'
        return string1

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        lst = []
        # a = 0
        # b = 0
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                lst.append((i, j))

        lst.append((3, 7))

        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        lst_to_return = []

        # for car_key, car_val in self.__cars.items():
        #     curr = car_val.possible_moves()
        #     for move, des in curr.items():
        #         lst_to_return.append((car_key, move, des))
        for car_key, car_val in self.__cars.items():
            curr = car_val.possible_moves()
            for move in curr:

                a, b = car_val.movement_requirements(move)[0]

                if not (0 <= a <= 6 and 0 <= b <= 6):
                    continue

                if self.__board[a][b] == "_":
                    lst_to_return.append((car_key, move, curr[move]))

        return lst_to_return

        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """

        a, b = coordinate

        if self.__board[a][b] == "_":
            return None
        else:
            return self.__board[a][b]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        already_has_this_name = False
        for lst in self.__board:
            if car.get_name() in lst:
                already_has_this_name = True

        if already_has_this_name:
            return False

        car_coor = car.car_coordinates()
        for place in car_coor:
            a, b = place

            if not (0 <= a <= 6 and 0 <= b <= 6):
                return False

            if self.__board[a][b] != "_":
                return False

        if len(car_coor) > 7:
            return False

        car_coor = car.car_coordinates()
        for place in car_coor:
            if place not in self.cell_list():
                return False

        for place in car_coor:
            a, b = place
            self.__board[a][b] = car.get_name()

        self.__cars[car.get_name()] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        x = self.__cars[name].possible_moves()

        if movekey not in self.__cars[name].possible_moves():
            return False


        board2 = copy.deepcopy(self.__board)

        flag1 = True
        flag2 = True

        if movekey == "r":
            for i in range(7):
                if self.__board[i][6] == name:
                    if i != 3:
                        return False

            for count, lst in enumerate(self.__board):
                for count2, element in enumerate(lst):
                    if element == name and self.__board[count][count2 - 1] != name and flag1:
                        self.__board[count][count2] = "_"
                        flag1 = False

                    if element == "_" and self.__board[count][count2 - 1] == name and flag2:
                        self.__board[count][count2] = name
                        flag2 = False

        if movekey == "l":

            for i in range(7):
                if self.__board[i][0] == name:
                    return False

            for count, lst in enumerate(self.__board):
                for count2, element in enumerate(lst):
                    if element == name and self.__board[count][count2 - 1] == "_" and flag1:
                        self.__board[count][count2 - 1] = name
                        flag1 = False

                    if element != name and self.__board[count][count2 - 1] == name and flag2:
                        self.__board[count][count2 - 1] = "_"
                        flag2 = False


        if movekey == "u":
            for i in range(7):
                if self.__board[0][i] == name:
                    return False

            for count, lst in enumerate(self.__board):
                for count2, element in enumerate(lst):
                    if element == name and count2 != 7 and self.__board[count - 1][count2] == "_" and flag1:
                        self.__board[count - 1][count2] = name
                        flag1 = False

                    if element != name and count2 != 7 and self.__board[count - 1][count2] == name and flag2:
                        self.__board[count - 1][count2] = "_"
                        flag2 = False


        if movekey == "d":
            for i in range(7):
                if self.__board[6][i] == name:
                    return False

            for count, lst in enumerate(self.__board):
                for count2, element in enumerate(lst):
                    if element == name and self.__board[count - 1][count2] != name and flag1:
                        self.__board[count][count2] = "_"
                        flag1 = False

                    if element == "_" and count2 != 7 and self.__board[count - 1][count2] == name and flag2:
                        self.__board[count][count2] = name
                        flag2 = False

        if not flag1 and not flag2:
            return True
        else:
            self.__board = board2
            return False

