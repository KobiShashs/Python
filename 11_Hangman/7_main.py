def check_valid_input(letter_guessed,old_letters_guessed):
    if(len(a)>1):
        if(not a.isalnum()):
          return "X";
        else:
            old_letters_guessed+=a;
    else:
        if(not a.isalnum()):
            old_letters_guessed+=a;
        else:
            return True;  

def print_welcome_prompt():
    HANGMAN_ASCII_ART = '''  _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/ '''

print(HANGMAN_ASCII_ART)
MAX_TRIES = 6
print("You have",MAX_TRIES,"tries")


# word = input("Please insert a word: ")
# print(word)
# print("_ _ _ _ _ _")
a = input("Guess a letter: ")
print(is_valid_input(a))
