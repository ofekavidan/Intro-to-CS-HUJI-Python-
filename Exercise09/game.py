#############################################################
# FILE : game.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise9 2021
# HELPED BY:
#############################################################

import sys
from car import Car
from board import Board
from helper import *


class Game:
    """
    A class that represents a game-type object.
    Through it we can run the game once, and in fact as many times as we want
    """


    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board
        self.colorlist = []

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it.

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        kelet = input("type the color and the direction of the car (for example: 'Y,d') ")

        if kelet == "!":
            return "!"

        if len(kelet) != 3:
            return False

        if kelet[1] != ",":
            return False

        color = kelet[0]
        direction = kelet[2]





        colorlst = ["Y","B","O","G","W","R"]
        directionlst = ["r", "l", "u", "d"]

        if color not in self.colorlist:
            return False

        if color not in colorlst:
            return False
        if direction not in directionlst:
            return False

        self.__board.move_car(color, direction)



        return True


    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        while (self.__board.cell_content(self.__board.target_location()) is None):
            temp = self.__single_turn()

            if(not temp):
                print("input not valid")
            else:
                if temp == "!":
                    break
                else:
                    print(self.__board)




        return None




if __name__== "__main__":
    colorlst = ["Y", "B", "O", "G", "W", "R"]

    board1 = Board()
    dict_cars = dict(load_json(sys.argv[1]))

    lst = []
    print(board1)

    for car in dict_cars:
        location = tuple(dict_cars[car][1])
        name = car
        length = dict_cars[car][0]
        orientation = dict_cars[car][2]

        if orientation != 1 and orientation != 0:
            continue

        if length != 2 and length != 3 and length != 4:
            continue

        if car not in colorlst:
            continue

        lst.append(car)
        car1 = Car(car, length, location, orientation)
        board1.add_car(car1)



    print(board1)


    game = Game(board1)
    game.colorlist = lst
    game.play()
