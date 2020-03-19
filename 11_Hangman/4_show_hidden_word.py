def show_hidden_word(secret_word, old_letters_guessed):
    res=""
    if(len(old_letters_guessed)==0):
        for c in secret_word:
            res+=("_ ")
        print(res)
        return
    arr1 = list(secret_word)
    arr2 = list(old_letters_guessed)
    i = 0
    while(i < len(arr1)):
        if(str(arr1[i]) == str(arr2[i])):
            res+=arr1[i]+" "
        else:
            res+=("_")+" "
        i += 1

    print(res)

secret_word = "splimq"
old_letters_guessed = []
print(show_hidden_word(secret_word, old_letters_guessed))
# m _ m m _ _ s
