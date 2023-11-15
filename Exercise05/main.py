def find_words(word_list, matrix, directions):
    """This function gets a word list, a matrix and directions (string)
    it returns the appropriate words which appeared in tha matrix by the appropriate directions"""
    list_of_found_words = []
    save_each_row = ""
    save_each_row_temp = ""
    if ("r" in directions):
        save_each_row = find_right(matrix, save_each_row)

    if ("l" in directions):
        save_each_row_temp = ""
        save_each_row_temp += find_right(matrix, save_each_row_temp)
        save_each_row += save_each_row_temp[::-1]

    if ("d" in directions):
        save_each_row = find_down(matrix, save_each_row)

    if ("u" in directions):
        save_each_row_temp = ""
        save_each_row_temp = find_down(matrix, save_each_row_temp)
        save_each_row += save_each_row_temp[::-1]

    if ("w" in directions):
        save_each_row += return_w_diagonal(matrix)

    if ("y" in directions):
        save_each_row += return_y_diagonal(matrix)

    if ("z" in directions):
        save_each_row_temp = ""
        save_each_row_temp += return_w_diagonal(matrix)
        save_each_row += save_each_row_temp[::-1]

    if ("x" in directions):
        save_each_row_temp = ""
        save_each_row_temp += return_y_diagonal(matrix)
        save_each_row += save_each_row_temp[::-1]

    for i in word_list:
        if str(i) in save_each_row:
            list_of_found_words.append((i, count_occurrences(save_each_row, i)))

    return list_of_found_words


def find_down(matrix, save_each_row):
    "This function gets a matrix and returns a string which contain the downs columns in the matrix"
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            save_each_row += matrix[j][i]
        save_each_row += "\n"
    return save_each_row


def find_right(matrix, save_each_row):
    "This function gets a matrix and returns a string which contain the rights rows in the matrix"
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


def read_wordlist(filename):
    """This function gets a filename (or his path in the computer) that contains words
    and returns a list of these words"""
    command = open(filename, "r")
    string_of_words = command.read()
    list_of_words = string_of_words.split("\n")

    command.close()
    return list_of_words


def read_matrix(filename):
    """This function gets a filename (or his path in the computer) that contains matrix
        and returns the matrix in list type"""
    command = open(filename, "r")
    string_of_letters = command.read()
    list_of_words = string_of_letters.split("\n")
    repaired_list_of_words = []

    for i in list_of_words:
        repaired_list_of_words.append(i.split(","))

    command.close()
    return repaired_list_of_words

if __name__ == '__main__':
    print(read_wordlist("word_list.txt"))
