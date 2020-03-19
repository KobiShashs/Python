def choose_word(file_path, index):
    f = open(str(file_path), "r")
    data = f.read()
    res = ()
    words = list(data.split(' '))
    res += (words[index],)
    unique_words = set(data.split(' '))
    res += (len(unique_words),)
    return res

#print(choose_word(r"C:\Python\hangman.txt", 3))
#(9, 'broadly')
#print(choose_word(r"C:\Python\hangman.txt", 6))
#(9, 'song')


def show_hidden_word(secret_word, old_letters_guessed):
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


#secret_word = "splimq"
# old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
# show_hidden_word(secret_word, old_letters_guessed)
#show_hidden_word(secret_word, [])
#show_hidden_word(secret_word, [])
#show_hidden_word("cat", ['t'])
#show_hidden_word("cat", ['T'])
# s p _ i m _
# _ _ _ _ _ _


def check_valid_input(letter_guessed, old_letters_guessed):
    if(len(letter_guessed) > 1):
        return False
    elif(not str(letter_guessed).isalpha()):
        return False
    elif(letter_guessed in old_letters_guessed):
        return False
    elif((len(letter_guessed) == 1) and (str(letter_guessed).isalpha()) and (letter_guessed not in old_letters_guessed)):
        return True
    return False

#old_letters = ['a', 'b', 'c']
#print("&&&&&&&&&&&&&&&&&&&&&&&&&")
#print(check_valid_input('C', old_letters))
#False
#print(check_valid_input('ep', old_letters))
#False
#print(check_valid_input('$', old_letters))
#False
#print(check_valid_input('s', old_letters))
#False
#print("&&&&&&&&&&&&&&&&&&&&&&&&&")
def letter_contains_in_list(letter_guessed, old_letters_guessed):
    if (str(letter_guessed).lower() in str(old_letters_guessed).lower()):
        print(":(")
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    print(letter_guessed,old_letters_guessed)
    if(check_valid_input(letter_guessed, old_letters_guessed) and (not letter_contains_in_list(letter_guessed, old_letters_guessed))):
        old_letters_guessed += letter_guessed
        return False
    elif ((not check_valid_input(letter_guessed, old_letters_guessed)) or(letter_contains_in_list(letter_guessed, old_letters_guessed))):
        print("X")
        old_letters_guessed.sort()
        pos = 1
        for x in old_letters_guessed:
            if(pos < len(old_letters_guessed)):
                print(str(x), end=" -> ")
            else:
                print(str(x), end="")
            pos += 1
        print()
        return False
    return True


old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed('A', old_letters))
print(try_update_letter_guessed('s', old_letters))
print(try_update_letter_guessed('$', old_letters))
print(try_update_letter_guessed('d', old_letters))
# print(old_letters)
#print(try_update_letter_guessed('A', old_letters))
# print(old_letters)
# X
# a -> c -> f -> p
# False
#print(try_update_letter_guessed('ep', old_letters)
# print(old_letters)
# True
# ['a', 'p', 'c', 'f', 's']
# try_update_letter_guessed('$', old_letters)
# print(old_letters)
# X
# a -> c -> f -> p -> s
# False
# try_update_letter_guessed('d', old_letters)
# print(old_letters)
# True
# ['a', 'p', 'c', 'f', 's', 'd']
#print("***")
#old_letters = []
#print("old_letters", old_letters)
#try_update_letter_guessed('^', old_letters)
#print("old_letters", old_letters)
#try_update_letter_guessed('T', old_letters)
#print("old_letters", old_letters)
#try_update_letter_guessed('b', old_letters)
#print("old_letters", old_letters)
#print("***")


def choose_word(file_path, index):
    f = open(str(file_path), "r")
    data = f.read()
    res = ()
    words = list(data.split(' '))
    res += (words[index],)
    unique_words = set(data.split(' '))
    res += (len(unique_words),)
    return res


#print(choose_word(r"C:\Python\hangman.txt", 3))
#(9, 'broadly')
#print(choose_word(r"C:\Python\hangman.txt", 6))
#(9, 'song')


def check_win(secret_word, old_letters_guessed):
    if secret_word in old_letters_guessed:
        return True
    return False
