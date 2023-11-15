#############################################################
# FILE : ex7.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise7 2021
# HELPED BY: https://bit.ly/3C9RjKV , https://youtu.be/5_6nsViVM00 ,
#############################################################

from typing import Any, Tuple, List

def print_to_n(n: int) -> None:
    """This function gets a number (n), and prints all the numbers from 1 until n"""
    if n >= 1:
        print_to_n(n - 1)
        print(n)


def digit_sum(n: int) -> int:
    """This function gets a number (n), and returns its sum of digits"""
    if n == 0:
        return 0
    return n % 10 + digit_sum(int(n / 10))


def is_prime(n: int) -> bool:
    """This function gets a number (n), and returns true if the number is prime. False otherwise
    it also helped by has_division_smaller_than function, to make the problem easier"""
    if n == 1:
        return False
    if n < 1:
        return False
    return not has_division_smaller_than(n, n)


def has_division_smaller_than(n: int, i: int) -> bool:
    """This function gets a number (n)
    and returns true if there's a number which divide n and smaller than i
    I made it to help is_prime function"""
    if i == 2:
        return False
    return n % (i - 1) == 0 or (has_division_smaller_than(n, i - 1))


def print_sequences(char_list: List[str], n: int) -> None:
    """This function gets a list of chars and prints all possible sequences (if their length is n)
    it also helped by print_sequences_helper to make the problem easier"""
    print_sequences_helper(char_list, n, "")


def print_sequences_helper(char_list: List[str], n: int, resultstring: str) -> None:
    """This function help print_sequences:
     it collects the sequences into resultstring and returns it at the end of the function

     its acting this way:
     first we save and 'lock' the first letter (the for loop using all possibilities from char_list)
     than, we send the resultstring again, with the first letter 'lock'
     than, we save and lock the second letter ect.
     than finally, when we got to the base case (the length of resultstring is n), we can print resultstring"""
    if len(resultstring) == n:
        print(resultstring)
        return

    for char in char_list:
        print_sequences_helper(char_list, n, (resultstring + char))


def print_no_repetition_sequences(char_list: List[str], n: int) -> None:
    """This function gets a list of chars, and a number (n).
    it returns all possible sequences (if their length is n, and they don't contain the same letter twice.
    it also helped by print_no_repetition_sequences_helper to make the problem easier"""
    print_no_repetition_sequences_helper(char_list, n, "")


def print_no_repetition_sequences_helper(char_list: List[str], n: int, resultstring: str) -> None:
    """This function help print_sequences_sequences_helper:
     it collects the sequences into resultstring and returns it at the end of the function

     its acting this way:
     first we save and 'lock' the first letter (the for loop using all possibilities from char_list)
     than, we send the resultstring again, with the first letter 'lock'
     than, we save and lock the second letter ect.

     than finally, when we got to the base case (the length of resultstring is n and don't has repetition),
      we can print resultstring"""
    if len(resultstring) == n:
        for i in range(len(resultstring)):
            for j in range(len(resultstring)):
                if resultstring[i] == resultstring[j] and i != j:
                    return

        print(resultstring)
        return

    for char in char_list:
        print_no_repetition_sequences_helper(char_list, n, resultstring + char)


def parentheses(n: int) -> List[str]:
    """This function gets an integer and returns all possible brackets sequences in a list,
    only if they are a valid mathematical expression. for example: 2 -> [()(), (())]
    it helped by parentheses_helper function"""
    lst: List[str] = []
    parentheses_helper(n, 0, 0, "", lst)
    return lst


def check_balance_of_brackets(collector: str) -> bool:
    """This function gets a string which contains a certain number of brackets
    it returns True if it is a valid mathematical expression, false otherwise"""
    opener = ['(']
    closer = [')']
    stack = []
    for char in collector:
        if char in opener:
            stack.append(char)
        elif char in closer:
            pos = closer.index(char)
            if len(stack) > 0 and stack[-1] == opener[pos]:
                stack.pop()
            else:
                return False
    return True if not stack else False


def parentheses_helper(n: int, n_open: int, n_close: int, collector: str, lst: List[str]) -> None:
    """This function help parentheses function above.
    it helped by check_balance_of_brackets this way:
    parentheses_helper send every possible brackets expression.
    if it is a valid mathematical expression, the function will append it to the list (lst)"""
    if n_open == n and n_close == n:
        if check_balance_of_brackets(collector):
            lst.append(collector)
            return
    if n_open < n:
        parentheses_helper(n, n_open + 1, n_close, collector + "(", lst)
    if n_close < n:
        parentheses_helper(n, n_open, n_close + 1, collector + ")", lst)


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """This function simulates hanoi game"""
    if n <= 0:
        return
    if n <= 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        play_hanoi(hanoi, 1, src, dst, temp)
        play_hanoi(hanoi, n - 1, temp, dst, src)


def flood_fill(image: List[List[str]], start: Tuple[int, int]) -> None:
    """This function simulates water that begins to flow in a maze and fills it all"""
    if image[start[0]][start[1]] == "*":
        return

    if image[start[0]][start[1]] == ".":
        image[start[0]][start[1]] = "*"
        flood_fill(image, (start[0] - 1, start[1]))
        flood_fill(image, (start[0] + 1, start[1]))
        flood_fill(image, (start[0], start[1] + 1))
        flood_fill(image, (start[0], start[1] - 1))


