#############################################################
# FILE : wordsearch.py
# WRITER : Ofek Avidan , ofek.avidan
# EXERCISE : intro2cse exercise5 2021
# HELPED BY: https://bit.ly/3BIW3H9 , https://bit.ly/3i5S67q
#############################################################
import re
import sys
import os.path


def read_wordlist(filename):
    """This function gets a filename (or his path in the computer) that contains words
    and returns a list of these words"""
    command = open(filename, "r")
    string_of_words = command.read()  # get the word list

    list_of_words = string_of_words.split("\n")  # divide the list by using split function

    if list_of_words[len(list_of_words) - 1] == "":  # get rid of empty strings (if exist)
        list_of_words.pop()

    list_of_words[:] = [x for x in list_of_words if x]

    command.close()
    return list_of_words


def read_matrix(filename):
    """This function gets a filename (or his path in the computer) that contains matrix
        and returns the matrix in list type"""
    command = open(filename, "r")
    string_of_letters = command.read()  # get the matrix
    list_of_words = string_of_letters.split("\n")  # divide the list by using split function
    repaired_list_of_words = []

    command.close()

    if list_of_words[len(list_of_words) - 1] == "":  # get rid of empty strings (if exist)
        list_of_words.pop()

    list_of_words[:] = [x for x in list_of_words if x]

    for i in list_of_words:
        repaired_list_of_words.append(i.split(","))  # split it into list of lists

    return repaired_list_of_words


def find_words(word_list, matrix, directions):
    """This function gets a word list, a matrix and directions (string)
    it returns the appropriate words which appeared in tha matrix by the appropriate directions"""
    list_of_found_words = []
    save_each_row = ""
    if "r" in directions:
        save_each_row = find_right(matrix, save_each_row)
    if "l" in directions:
        save_each_row += find_right(matrix, "")[::-1] + "\n"  # reverse the right direction
    if "d" in directions:
        save_each_row = find_down(matrix, save_each_row)
    if ("u" in directions):
        save_each_row += find_down(matrix, "")[::-1] + "\n"  # reverse the down direction
    if ("w" in directions):
        save_each_row += return_w_diagonal(matrix)
    if ("y" in directions):
        save_each_row += return_y_diagonal(matrix)
    if ("z" in directions):
        save_each_row += return_w_diagonal(matrix)[::-1] + "\n"    # reverse the w diagonal direction
    if ("x" in directions):
        save_each_row += return_y_diagonal(matrix)[::-1] + "\n"    # reverse the y diagonal direction
    for i in word_list:
        if str(i) in save_each_row:
            list_of_found_words.append((i, count_occurrences(save_each_row, i)))
    return list_of_found_words


def find_down(matrix, save_each_row):
    "This function gets a matrix and returns a string which contain the downs columns in the matrix"
    if not len(matrix):
        return ""

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            save_each_row += matrix[j][i]
        save_each_row += "\n"
    return save_each_row


def find_right(matrix, save_each_row):
    "This function gets a matrix and returns a string which contain the rights rows in the matrix"
    if not len(matrix):
        return ""

    for row in matrix:
        for i in row:
            save_each_row += str(i)
        save_each_row += "\n"
    return save_each_row


def count_occurrences(the_row, the_word):
    """This function gets string and word to check
    it also count the overlapping words (if they're exist)"""
    number_of_occurrences = 0
    start_of_the_string = 0

    while start_of_the_string < len(the_row):
        position = the_row.find(the_word, start_of_the_string)
        if position != -1:
            start_of_the_string = position + 1

            number_of_occurrences += 1
        else:
            break

    return number_of_occurrences


def return_w_diagonal(matrix):
    """This function gets a matrix and returns string of its w diagonal"""

    if not len(matrix):
        return ""

    col = len(matrix[0])
    row = len(matrix)
    fdiag = [[] for _ in range(row + col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -row + 1

    fdiag_str = ""

    for x in range(col):
        for y in range(row):
            fdiag[x + y].append(matrix[y][x])
            bdiag[x - y - min_bdiag].append(matrix[y][x])

    for i in fdiag:
        for j in i:
            fdiag_str += str(j)
        fdiag_str += "\n"

    return (fdiag_str)


def return_y_diagonal(matrix):
    """This function gets a matrix and returns string of its y diagonal"""
    if not len(matrix):
        return ""

    col = len(matrix[0])
    row = len(matrix)
    fdiag = [[] for _ in range(row + col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -row + 1

    bdiag_str = ""

    for x in range(col):
        for y in range(row):
            fdiag[x + y].append(matrix[y][x])
            bdiag[x - y - min_bdiag].append(matrix[y][x])

    for i in bdiag:
        for j in i:
            bdiag_str += str(j)
        bdiag_str += "\n"

    return (bdiag_str)


def write_output(results, filename):
    """This function gets list of results
     and updates the appropriate file (by using its filename or his path)"""
    results_string = ""
    for element in results:
        results_string += str(element)
        results_string += "\n"

    # get rid of excess brackets and spaces:

    results_string = results_string.replace("(", "")
    results_string = results_string.replace(")", "")
    results_string = results_string.replace("'", "")
    results_string = results_string.replace(" ", "")

    command = open(filename, "w")
    command.write(results_string)

    command.close()

def check_input_args(args):
    """This function check if our arguments 'passed' all the tests
    for instance: 4 arguments, appropriate directions etc.
    if we did passed all the tests, the error message will be None"""
    message = None  # initial boot of the error message
    if len(args) != 4:
        message = "Please enter all 4 parameters"
    else:
        word_file = args[0]
        matrix_file = args[1]
        output_file = args[2]
        directions = args[3]

        if all(char in "lrudxyzw" for char in directions):
            if not os.path.isfile(word_file) or not os.path.isfile(matrix_file):
                if not os.path.isfile(word_file):
                    message = "enter an active path (word_file)"
                else:
                    message = "enter an active path (matrix_file)"
        else:
            message = "enter proper direction string"

    return message


def run_crossword():
    """The main function. this function uses all other functions to start the game on.
    It also communicates with the user (remote) by getting the appropriate parameters"""
    arguments = sys.argv[1:] # get the arguments from the terminal. get rid of the first argument (wordsearch.py)
    if check_input_args(arguments) == None:  # if we passed all the 'tests' of check_input_args
        word_file = arguments[0]  # enter data to our variables appropriately
        matrix_file = arguments[1]  # enter data to our variables appropriately
        output_file = arguments[2]  # enter data to our variables appropriately
        directions = arguments[3]  # enter data to our variables appropriately
        word_list = read_wordlist(word_file)  # send the appropriate path to the read function
        matrix = read_matrix(matrix_file)  # send the appropriate path to the read function
        last_char_of_word_list = word_list[len(word_list) - 1]
        if last_char_of_word_list == "\n":
            word_list = word_list[:len(word_list) - 1]  # get rid of the last new line (if exist)
        last_char_of_matrix = matrix[len(matrix) - 1]
        if last_char_of_matrix == "\n":
            matrix = matrix[:len(word_list) - 1]  # get rid of the last new line (if exist)
        if not matrix:  # checking if our matrix is empty
            result_list = ""
            write_output(result_list, output_file)  # feed the results as an empty string
        else:
            result_list = find_words(word_list, matrix, directions)
            write_output(result_list, output_file)
    else:
        print(check_input_args(arguments))


if __name__ == '__main__':
    run_crossword()
