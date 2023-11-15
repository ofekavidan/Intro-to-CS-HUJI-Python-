#############################################################
# FILE : nonogram.py
# WRITER1 : Ofek Avidan , ofek.avidan , 318879574
# WRITER2: Tohar Simchi , toharsimchi , 209207876
# EXERCISE : intro2cse exercise8 2021
# HELPED BY: Tirgul 8 (Subset Sum), https://bit.ly/3lJ4WLd ,
# WHY I CHOSE -1 OPTION: It was easier programmingly and didn't require a double code
#############################################################
import copy
import time



def constraint_satisfactions(n, blocks):
    """
    This function gets number of squares and the number of squares we want to dark
    it returns all the possible options of the squares

    examples:

    constraint_satisfactions(3, [1]) -> [ [1, 0, 0], [0, 1, 0] , [0, 0, 1]]
    constraint_satisfactions (3, [2]) -> [ [1, 1, 0], [0, 1, 1] ]
    constraint_satisfactions (3, [1, 1]) -> [ [1, 0, 1] ]
    constraint_satisfactions (4, [1, 1]) -> [ [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1]]
    constraint_satisfactions (5, [2, 1]) -> [ [1, 1, 0, 1, 0] , [1, 1, 0, 0, 1], [0, 1, 1, 0, 1] ]
    :param n: number of squares
    :param blocks: number of painted squares
    :return: all possible options of the row
    """


    return _helper_constraint_satisfactions(n, blocks, [], 0, 0, 0)


# auxiliaries functions constraint_satisfactions()
def _helper_constraint_satisfactions(n, blocks, temp_row=[], curr_blck=0, i=0, blck_indx=0):
    if len(blocks)>1:
        if len(temp_row) == n and curr_blck!=0 and curr_blck!=blocks[-1]:        # todo
            return []
    if len(temp_row)>n:
        return []
    if sum(temp_row) == sum(blocks) and len(temp_row)==n:  # all the blocks are in temp row and its in the right length
        res = [temp_row]
        return res

    results = []
    if len(blocks)>1:
        if i>0 and temp_row[i-1] == 0:  # make sure that the blocks are appends by their order
            if curr_blck!=0 and curr_blck != blocks[blck_indx-1]:
                return []
        if blck_indx > len(blocks):
            return []
        if curr_blck == blocks[blck_indx-1]:
            temp_row.append(0)
            curr_blck = 0
            results+=_helper_constraint_satisfactions(n, blocks, temp_row[:], 0, i + 1, blck_indx)# + 1)
    elif i>0 and temp_row[i-1] == 0:  # make sure that the blocks are appends by their order
        if blocks and curr_blck!=0 and curr_blck!=blocks[0]:
            return []

    temp_row.append(0)
    #if temp_row[i-1] != 0:
    #    results += _helper_constraint_satisfactions(n, blocks, temp_row[:], curr_blck, i + 1, blck_indx + 1)
    #else:
    results += _helper_constraint_satisfactions(n, blocks, temp_row[:], curr_blck, i + 1, blck_indx)
    temp_row.pop()

    temp_row.append(1)
    if i-1 < 0 or temp_row[i-1]==0:
        blck_indx += 1
    results += _helper_constraint_satisfactions(n, blocks, temp_row[:], curr_blck + 1, i + 1, blck_indx)
    temp_row.pop()
    if len(results)>1:
        filter_results(results)
    return results


def filter_results(results):

    # for i in range(len(results)-1):
    #     if results[i] in results[:i]+results[i+1:]:
    #         results.pop(i)


    for result in results:
        if results.count(result) > 1:
            results.remove(result)

# end auxiliaries functions constraint_satisfactions()





###########################


def is_valid_list(n, blocks, innerlst):
    """
    This function gets a list of painted/unpainted squares, and a block
    it returns true if the list is valid, false otherwise
    :param n: number of squares (or in this case, lst length)
    :param blocks: number of the squares we want to paint. for instance => [2,1]
    :param innerlst: the list we want to compare (to the blocks) and check if valid
    :return: true if the list is valid, false otherwise
    """
    counterlst = []
    counter = 0

    if innerlst == blocks:
        return True

    if sum(innerlst) == 0 and sum(blocks) == 0 and all([v == 0 for v in innerlst]) and all([v == 0 for v in blocks]):
        return True

    for element in innerlst:
        if element == 0:
            if counter != 0:
                counterlst.append(counter)
                counter = 0
        else:
            counter += 1

    if counter != 0:
        counterlst.append(counter)

    if counterlst == blocks:
        return True
    else:
        return False


def filter_list(n, blocks, lst):
    """
    This function gets list of lists (of possible solutions),
    and filters the list (than returns it).
    :param n: number of squares (or in this case, lst length)
    :param blocks: number of the squares we want to paint. for instance => [2,1]
    :param lst: the list we want to filter
    :return: the filtered list
    """
    flag = True

    while flag:
        flag = False
        for innerlst in lst:
            if not is_valid_list(n, blocks, innerlst):
                flag = True
                lst.remove(innerlst)

    return lst


def row_variations(row, blocks):
    """
    This function gets a list of squares, and a number of squares that we want to paint
    and returns all the possible options to paint these squares.

    examples:

    row_variations([1, 1, -1, 0], [3]) -> [[1, 1, 1, 0]]
    row_variations([-1, -1, -1, 0], [2]) -> [[0, 1, 1, 0], [1, 1, 0, 0]]
    row_variations([-1, 0, 1, 0, -1, 0], [1,1]) -> [[0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0]]
    row_variations([-1, -1, -1] , [1]) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
    row_variations([0, 0, 0] , [1]) -> [ ]
    row_variations([0, 0, -1, 1, 0] , [3]) -> [ ]
    row_variations([0, 0, -1, 1, 0] , [2]) -> [ [0, 0, 1, 1, 0]]
    row_variations([0, 0, 1, 1, 0] , [2]) -> [ [0, 0, 1, 1, 0]]

    :param row: the row itself. list that contains number of squares
    :param blocks: the number of squares we want to paint
    :return: all the possible options to paint these squares.
    """
    return filter_list(len(row), blocks, row_variations_helper(row, blocks, [], 0))


def row_variations_helper(row, blocks, partial, index):
    if index == len(row):
        res = []
        if sum(partial) == sum(blocks):
            res.append(partial[:])
        return res

    solution_list = []

    if row[index] == -1:
        partial.append(1)

        solution_list += row_variations_helper(row, blocks, partial, index + 1)
        partial.pop()

        partial.append(0)
        solution_list += row_variations_helper(row, blocks, partial, index + 1)

        partial.pop()

    else:
        if row[index] == 0:
            partial.append(0)
            solution_list += row_variations_helper(row, blocks, partial, index + 1)
            partial.pop()
        else:
            if row[index] == 1:
                partial.append(1)
                solution_list += row_variations_helper(row, blocks, partial, index + 1)
                partial.pop()

    return solution_list


def intersection_row(rows):
    """
    This function gets a list of lists, and returns the appropriate overlapping squares

    examples:

    intersection_row([[0, 0, 1], [0, 1, 1], [0, 0, 1]]) -> [0, -1, 1]
    intersection_row([[0, 1, -1], [-1, -1, -1]]) -> [0, 1, -1] or [-1, -1, -1]
    :param rows: list of lists (rows)
    :return: the appropriate overlapping squares
    """
    lst = []

    if not rows:
        return None

    if len(rows) == 1:
        lst = rows[0]
    else:
        for i in range(len(rows[0])):
            flag = True
            for j in range(len(rows) - 1):
                if rows[j][i] != rows[j + 1][i]:
                    flag = False
            if flag:
                lst.append(rows[j][i])
            else:
                lst.append(-1)

    return lst


def solve_easy_nonogram(constraints):
    """
    Function that mimics a human solution method for black and solved:
    the function will check which squares must be
    Black / white in each row (according to the overlap of all options), and color them accordingly.

    :param constraints: The Nonogram itself. for example: [[[1,1], [0]], [[1], [0], [1]]]]
    :return: Solved game board (as much as possible)
    """
    flag = True
    row_length = len(constraints[0])
    col_length = len(constraints[1])

    lst = [[-1] * col_length] * row_length

    while flag:
        flag = False
        # rows:
        for i in range(row_length):
            if lst[i] != intersection_row(row_variations(lst[i], constraints[0][i])):
                if intersection_row(row_variations(lst[i], constraints[0][i])) is None:
                    return None

                lst[i] = intersection_row(row_variations(lst[i], constraints[0][i]))
                flag = True

        lst = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]

        for i in range(col_length):
            if lst[i] != intersection_row(row_variations(lst[i], constraints[1][i])):
                if intersection_row(row_variations(lst[i], constraints[1][i])) is None:
                    return None

                lst[i] = intersection_row(row_variations(lst[i], constraints[1][i]))
                flag = True

        lst = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]

    return lst


def solve_easy_nonogram_with_list(constraints, lst):
    """
    Function that mimics a human solution method for black and solved:
    the function will check which squares must be
    Black / white in each row (according to the overlap of all options), and color them accordingly.
    this time we also get a list, with some black/white squares

    :param constraints: The Nonogram itself. for example: [[[1,1], [0]], [[1], [0], [1]]]]
    :param lst: list of a little bit solved squares
    :return: Solved game board (as much as possible)
    """
    flag = True
    row_length = len(constraints[0])
    col_length = len(constraints[1])

    while flag:
        flag = False
        # rows:
        for i in range(row_length):
            if lst[i] != intersection_row(row_variations(lst[i], constraints[0][i])):
                if intersection_row(row_variations(lst[i], constraints[0][i])) is None:
                    return None

                lst[i] = intersection_row(row_variations(lst[i], constraints[0][i]))
                flag = True

        lst = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]

        for i in range(col_length):
            if lst[i] != intersection_row(row_variations(lst[i], constraints[1][i])):
                if intersection_row(row_variations(lst[i], constraints[1][i])) is None:
                    return None

                lst[i] = intersection_row(row_variations(lst[i], constraints[1][i]))
                flag = True

        lst = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]

    return lst



def solve_nonogram(constraints):
    """
    Function that gets Nonogram game board constraints and returns a list of
    Solutions for the game.
    :param constraints: The Nonogram itself. for example: [[[1,1], [0]], [[1], [0], [1]]]]
    :return: Solved game board
    """

    row_length = len(constraints[0])
    col_length = len(constraints[1])
    lst = [[-1] * col_length] * row_length

    partsolution = solve_easy_nonogram(constraints)

    if partsolution is None:
        return None

    return _solve_nonogram_helper(constraints, partsolution, 0)


def _solve_nonogram_helper(constraints, solutionlst, index):
    """
        Helper for solve_nonogram function
        :param constraints: The Nonogram itself. for example: [[[1,1], [0]], [[1], [0], [1]]]]
        :param solutionlst: all possible solutions
        :param index: helps us to run over this function recursively
        :return: Solved game board
        """
    res = []
    solutionlst2 = copy.deepcopy(solutionlst)
    indexofrowoptions = len(row_variations(solutionlst[index], constraints[0][index]))
    for i in range(indexofrowoptions):
        solutionlst[index] = row_variations(solutionlst[index], constraints[0][index])[i]
        partial = solve_easy_nonogram_with_list(constraints, solutionlst)

        if partial is not None:
            res.append(partial)
            solutionlst[index] = solutionlst2[index]

    return res


