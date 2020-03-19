
def check_valid_input(letter_guessed, old_letters_guessed):
    if(len(letter_guessed) > 1):
        return False
    elif(not str(letter_guessed).isalpha()):
        return False
    elif(letter_guessed in old_letters):
        return False
    elif((len(letter_guessed) == 1) and (str(letter_guessed).isalpha()) and (letter_guessed not in old_letters)):
        return True
    return False


def letter_contains_in_list(letter_guessed, old_letters_guessed):
    return (str(letter_guessed).lower()) in (str(old_letters_guessed).lower())

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    print("0")
    if(check_valid_input(letter_guessed, old_letters) and (not letter_contains_in_list(letter_guessed,old_letters_guessed))):
        print("1")
        old_letters_guessed += letter_guessed
    elif ((not check_valid_input(letter_guessed, old_letters)) or(letter_contains_in_list(letter_guessed,old_letters_guessed))):
        print("2")
        print("X")
        old_letters.sort()
        pos = 1;
        for x in old_letters:
            if(pos<len(old_letters)):
                print(str(x), end=" -> ")
            else:
                print(str(x), end="")
            pos+=1
        print()

old_letters = []
print(old_letters)
char = "a"
try_update_letter_guessed(char, old_letters)
#old_letters = ['a', 'p', 'c', 'f']
#print(old_letters)
#try_update_letter_guessed('A', old_letters)
#print(old_letters)
# X
# a -> c -> f -> p
# False
#try_update_letter_guessed('s', old_letters)
#print(old_letters)
# True
#['a', 'p', 'c', 'f', 's']
#try_update_letter_guessed('$', old_letters)
#print(old_letters)
# X
# a -> c -> f -> p -> s
# False
#try_update_letter_guessed('d', old_letters)
#print(old_letters)
# True
#['a', 'p', 'c', 'f', 's', 'd']
