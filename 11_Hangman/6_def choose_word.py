def choose_word(file_path, index):
    f = open(str(file_path), "r")
    data = f.read()
    res = ();
    words = list(data.split(' '))
    res+=(words[index],)
    unique_words = set(data.split(' '))
    res+=(len(unique_words),)
    return res;

print(choose_word(r"C:\Python\hangman.txt", 3))
#(9, 'broadly')
print(choose_word(r"C:\Python\hangman.txt", 6))
#(9, 'song')