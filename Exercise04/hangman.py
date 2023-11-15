#############################################################
# FILE : ex4.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise4 2021
#############################################################


import hangman_helper
import copy


def update_word_pattern(word, pattern, letter):
    """This function gets a word, a pattern and a letter.
    Than updates the pattern if the letter was appropriate and returns the pattern"""

    indexes = []  #  which indexes contain the letter in the chosen word
    for i in range(len(word)):
        if word[i] == letter:
            indexes.append(i)

    #  turns the pattern into a list, so i could change the pattern in the appropriate index:
    lst = list(pattern)

    #  changes the appropriate index
    for j in indexes:
        lst[j] = letter

    #  turns the list back into a string and return it
    pattern = "".join(lst)
    return pattern

def run_single_game(words_list, score):
    """This function gets a words list and the score
    it runs a single game and returns the updated score"""

    word = hangman_helper.get_random_word(words_list)
    message = ""
    wrongs = []
    corrects = []
    num_guesses = 0
    pattern = "_" * len(word)


    hangman_helper.display_state(pattern, wrongs, score, "")

    while(("_" in pattern) and (score > 0)):
        choice, guess = hangman_helper.get_input()
        islow = str(guess).islower()

        if (choice == hangman_helper.LETTER):  #  chose letter
            if(len(guess) != 1 or not islow):
                message = "If you choose letter, enter only one lowercase letter"
            else:
                if (guess in wrongs or guess in corrects):
                    message = "you already chose that letter"
                else:
                    score = score - 1
                    pattern = update_word_pattern(word, pattern, guess)
                    if (guess in word):
                        n = str(word).count(guess)
                        score = score + (n * (n+1) // 2)
                        corrects.append(guess)
                    else:
                        wrongs.append(guess)



        if (choice == hangman_helper.WORD):  #  chose word
            score = score - 1
            if(word == guess):  #  if the chosen word is the right word
                number_of_letters = pattern.count("_")
                score = score + (number_of_letters * (number_of_letters+1) // 2)
                pattern = word
            else:
                if (score > 0):
                    message = "this isn't the word"
                    # hangman_helper.display_state(pattern, wrongs, score, "this isn't the word")
                else:
                    message = "this isn't the word, the word is " + word
                    score = 0
                    # hangman_helper.display_state(pattern, wrongs, score, messageword)

        if (choice == hangman_helper.HINT):  #  chose hint
            score = score - 1
            hints = filter_words_list(words_list, pattern, wrongs)
            hints_filtered = []

            if (len(hints) > hangman_helper.HINT_LENGTH):
                for i in range(0, hangman_helper.HINT_LENGTH, 1):
                    hints_filtered.append(hints[i*len(hints)//hangman_helper.HINT_LENGTH])

                hangman_helper.show_suggestions(hints_filtered)
            else:
                hangman_helper.show_suggestions(hints)

        if ("_" in pattern and score > 0):
            hangman_helper.display_state(pattern, wrongs, score, message)


    end_of_the_game(pattern, score, word, wrongs)

    return score


def end_of_the_game(pattern, score, word, wrongs):
    if score > 0:
        message = "you won the game!"
        hangman_helper.display_state(pattern, wrongs, score, message)
    else:
        message = "you lost the game, the word was " + word
        hangman_helper.display_state(pattern, wrongs, score, message)


def filter_words_list(words, pattern, wrong_guess_lst):
    """This function gets a list of words, a pattern, and a list of wrong guesses
    it returns only the appropriate list of words that can use as a hint"""

    lst = copy.deepcopy(words)

    #  filter by length
    flag = True
    while flag:
        flag = False
        for i in lst:
            if(len(i) != len(pattern)):
                lst.remove(i)
                flag = True

    #  filter by wrong guesses
    flag = True
    while flag:
        flag = False
        for j in lst:
            for x in wrong_guess_lst:
                if(x in j) and (j in lst):
                    lst.remove(j)
                    flag = True

    lst_to_delete = []

    #  filter by the appropriate index existing in the pattern
    #  in this for i'll take a new list and append it with values i need to delete
    for i in lst:
        counter = 0
        for x in pattern:
            if (x != "_"):
                if (i[counter] != x):
                    lst_to_delete.append(i)
            counter += 1

    not_common_list = [c for c in lst if c not in lst_to_delete]


    another_list_to_remove = []
    counter_of_lettters_in_list = 0
    counter_of_lettters_in_pattern = 0
    for i in not_common_list:
        for j in pattern:
            if (j != "_"):
                if (str(i).count(j) != pattern.count(j)):
                    another_list_to_remove.append(i)


    final_list = [t for t in not_common_list if t not in another_list_to_remove]



    return final_list


def main():
    """This function is the main program"""

    count_games = 1
    lst = hangman_helper.load_words()
    score = run_single_game(lst, hangman_helper.POINTS_INITIAL)
    if(score > 0):
        message = "you played " + str(count_games) + " games, and scored " + str(score)
        flag = hangman_helper.play_again(message)

        while(flag and score > 0):
            count_games += 1
            score = run_single_game(lst, score)
            if(score > 0):
                message = "you played " + str(count_games) + " games, and scored " + str(score)
                flag = hangman_helper.play_again(message)
            else:
                score = 0
                message = "you played " + str(count_games) + " games until the lose"
                flag = hangman_helper.play_again(message)
                if flag:
                    score = hangman_helper.POINTS_INITIAL


    else:
        score = 0
        message = "you played " + str(count_games) + " games until the lose"
        flag = hangman_helper.play_again(message)

        count_games = 0
        while (flag):
            count_games += 1
            score = hangman_helper.POINTS_INITIAL
            score = run_single_game(lst, score)
            if (score > 0):
                message = "you played " + str(count_games) + " games, and scored " + str(score)
                flag = hangman_helper.play_again(message)
            else:
                score = 0
                message = "you played " + str(count_games) + " games until the lose"
                flag = hangman_helper.play_again(message)




if __name__ == '__main__':
    main()



