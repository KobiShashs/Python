import subprocess as sys
import print_utils as pp
import game_utils as logic


def main():
    sys.call('cls', shell=True)
    pp.print_welcome_prompt()

    words_path = (r"C:\Python\hangman.txt")
    index = 3
    #words_path = (r"C:\Python\hangman.txt")
    #index = 3
    #words_path = input("File path: ")
    #index =  input("Index: ")

    info = logic.choose_word(words_path, index)
    print("tuple details:", info)
    print("word len:", info[1])
    print("you need to guess: ", info[0])
    old_letters_guessed = []
    pp.print_hangman(1)
    logic.show_hidden_word(info[0],old_letters_guessed)

    number_of_tries = 6
    number_of_errors = 0

    while(number_of_tries > number_of_errors):
        c = str(input("Guess a letter: "))
        if(logic.try_update_letter_guessed(c, old_letters_guessed)==False):
            number_of_errors+=1
        logic.show_hidden_word(info[0],old_letters_guessed)

        pp.print_hangman(number_of_errors+1)


if __name__ == "__main__":
    main()
