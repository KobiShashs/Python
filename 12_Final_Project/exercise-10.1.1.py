__author__ = "Kobi Shasha"

import subprocess as sys
import print_utils as pp


def main():
    sys.call('cls', shell=True)
    pp.print_welcome_prompt()

    words_path = (r"C:\Python\hangman.txt")
    index = 3
    # words_path = input("File path: ")
    # index =  input("Index: ")

    info = choose_word(words_path, index)
    secret_word = info[0]
    old_letters_guessed = []
    num_of_tries = 0
    pp.print_hangman(num_of_tries+1)
    show_hidden_word(info[0], old_letters_guessed)

    MAX_TRIES = 6
    while(num_of_tries < MAX_TRIES):
        letter_guessed = input("Guess a letter: ")
        if(not try_update_letter_guessed(letter_guessed, old_letters_guessed)):
            print(":(")
            num_of_tries += 1
            pp.print_hangman(num_of_tries+1)
            show_hidden_word(secret_word, old_letters_guessed)
        else:
            show_hidden_word(secret_word, old_letters_guessed)

    if(check_win(secret_word, old_letters_guessed)):
        print("WIN")
    else:
        print("LOSE")


def choose_word(file_path, index):
    """ return a tuple with the coosen word by index, and len of unuiqe words """
    f = open(str(file_path), "r")
    data = f.read()
    res = ()
    words = list(data.split(' '))
    res += (words[(index-1) % (len(words))],)
    unique_words = set(data.split(' '))
    res += (len(unique_words),)
    return res

#print(choose_word(r"C:\Python\hangman.txt", 3))
#(9, 'most')
#print(choose_word(r"C:\Python\hangman.txt", 15))
#(9, 'hangman')


def is_valid_input(letter_guessed):
    """ check if an input is a valid """

    if(len(letter_guessed) > 1) or (not str(letter_guessed).isalpha()):
        return False
    if(len(letter_guessed) == 1 and (str(letter_guessed).isalpha())):
        return True
    return False

# print(is_valid_input('a'))
# True
# print(is_valid_input('A'))
# True
# print(is_valid_input('$'))
# False
# print(is_valid_input("ab"))
# False
# print(is_valid_input("app$"))
# False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ check if  a user guess is valid or not """

    if(is_valid_input(letter_guessed) and (letter_guessed.lower() not in map(lambda x: x.lower(), old_letters_guessed))):
        old_letters_guessed += letter_guessed
        return True
    if((not is_valid_input(letter_guessed)) or (letter_guessed.lower() in map(lambda x: x.lower(), old_letters_guessed))):
        print("X")
        for c in sorted(old_letters_guessed):
            print(c+"".join(" -> "), end="")
        print()
        return False
    return False

#old_letters = []
#old_letters = ['a', 'p', 'c', 'f']
#print(try_update_letter_guessed('A', old_letters))
#print(try_update_letter_guessed('s', old_letters))
#print(try_update_letter_guessed('$', old_letters))
#print(try_update_letter_guessed('d', old_letters))


def check_win(secret_word, old_letters_guessed):
    """ check user guess the seret word """

    for c in secret_word:
        if(c not in old_letters_guessed):
            return False
    return True

#secret_word = "friends"
#old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
#print(check_win(secret_word, old_letters_guessed))
# False
#secret_word = "yes"
#old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
#print(check_win(secret_word, old_letters_guessed))
# True


def show_hidden_word(secret_word, old_letters_guessed):
    """ show the letters where user guess correct"""
    res = ""
    if(len(old_letters_guessed) == 0):
        for c in secret_word:
            res += ("_ ")
        print(res)
        return
    for c in secret_word:
        if(c.lower() in map(str.lower, old_letters_guessed)):
            res += c+" "
        else:
            res += "_ "
    print(res)


#secret_word = "broadly"
#old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
#show_hidden_word(secret_word, old_letters_guessed)
#show_hidden_word(secret_word, [])
#show_hidden_word(secret_word, [])
#show_hidden_word("cat", ['t'])
#show_hidden_word("cat", ['T'])
# s p _ i m _
# _ _ _ _ _ _

if __name__ == "__main__":
    main()
