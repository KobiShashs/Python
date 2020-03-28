
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    res = ""
    count = len(str(sentence).split(" "))
    print("count",count)
    gen = (words[word] for word in str(sentence).split(" "))
    while(count>0):
        res+=(next(gen)+" ")
        count-=1
    return res


    



print(translate("el gato esta en la casa"))
#the cat is in the house