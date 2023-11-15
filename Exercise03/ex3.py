#############################################################
# FILE : ex3.py
# EXERCISE : intro2cse exercise3 2021
#############################################################


def input_list():
    """This function inputs from the user some numbers, makes a list of them, and append the sum of them"""
    flag = True  # initial boot
    sum = 0  # initial boot
    lst = list()
    while (flag):
        num = input()
        if (num == ""):
            flag = False
            break
        else:
            sum += float(num)
            lst.append(float(num))

    lst.append(sum)
    return lst

def inner_product(vec_1, vec_2):
    """this function gets two lists of numbers and returns the sum of each index in both two lists"""
    sum = 0  # initial boot

    if (len(vec_1) == 0 and len(vec_2) == 0):
        return 0

    if(len(vec_1) != len(vec_2)):
        return None
    else:
        for x in range(len(vec_1)):
            sum += vec_1[x] * vec_2[x]

    return sum


def sequence_monotonicity(sequence):
    """this function gets a sequence and returns the type of the sequence (list of booleans)"""

    # Just to remind
    # 0 - up and eq
    # 1 - up
    # 2 - down and eq
    # 3 - down

    lst = list()
    lst = [True, True, True, True]

    if (len(sequence) <= 1):
        return lst

    for x in range(len(sequence) - 1):
        if (not (sequence[x] <= sequence[x + 1])):
            lst[0] = False
        if (not (sequence[x] < sequence[x + 1])):
            lst[1] = False
        if (not (sequence[x] >= sequence[x + 1])):
            lst[2] = False
        if (not (sequence[x] > sequence[x + 1])):
            lst[3] = False
    return lst


def monotonicity_inverse(def_bool):
    """This function gets list of booleans that describe which type of sequence the function should return"""

    lst_up_and_eq = [1,2,2,4]
    lst_up = [1,2,3,4]
    lst_down_and_eq = [4,2,2,1]
    lst_down = [4, 3, 2, 1]
    lst_eq = [1,1,1,1]
    lst_none = [1,-1,3,0]

    lst_up_and_eq_bool = sequence_monotonicity(lst_up_and_eq)
    lst_up_bool = sequence_monotonicity(lst_up)
    lst_down_and_eq_bool = sequence_monotonicity(lst_down_and_eq)
    lst_down_bool = sequence_monotonicity(lst_down)
    lst_eq_bool = sequence_monotonicity(lst_eq)
    lst_none_bool = sequence_monotonicity(lst_none)


    if(lst_up_and_eq_bool == def_bool):
        return lst_up_and_eq

    if(lst_up_bool == def_bool):
        return lst_up

    if(lst_down_and_eq_bool == def_bool):
        return lst_down_and_eq

    if(lst_down_bool == def_bool):
        return lst_down

    if (lst_eq_bool == def_bool):
        return lst_eq

    if (lst_none_bool == def_bool):
        return lst_none


    return None


# Took from lab3
def is_prime_very_fast(n):
    """This function runs on each number from 0 to n, (in this case, his root). return True if n is prime number"""
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def primes_for_asafi(n):
    """this function gets a number (n), and returns all the first n prime numbers"""
    counter = 0  # initial boot
    i = 0  # initial boot
    lst = list()

    while (counter != n):
        if is_prime_very_fast(i):
            counter += 1
            lst.append(i)
        i+=1

    return lst

def sum_of_vectors(vec_lst):
    """this function gets list of lists of vectors and return their sum"""
    out_length = len(vec_lst)
    inner_length = len(vec_lst[0])
    sumlst = list()

    counter = 0  # initial boot
    for x in range(inner_length):
        counter = 0  # initial boot
        for y in range(out_length):
            counter += vec_lst[y][x]
        sumlst.append(counter)

    return sumlst


def num_of_orthogonal(vectors):
    """this function gets a list of vectors and returns how many of them create 90 celsius degrees"""
    counter = 0  # initial boot

    for x in range(len(vectors)):
        for y in range(len(vectors)):
            if(y != x):
                if inner_product(vectors[x], vectors[y]) == 0:
                    counter += 1


    return (counter / 2)



