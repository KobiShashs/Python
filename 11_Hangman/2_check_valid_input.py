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


old_letters = ['a', 'b', 'c']
print(check_valid_input('C', old_letters))
# True
print(check_valid_input('ep', old_letters))
# False
print(check_valid_input('$', old_letters))
# False
print(check_valid_input('s', old_letters))
# True
