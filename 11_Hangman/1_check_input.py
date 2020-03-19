a = input("Guess a letter: ")
if(len(a)>1):
    if(not a.isalnum()):
        print("E3")
    else:
        print("E1")
else:
    if(not a.isalnum()):
        print("E2")
    else:
        print(a)    
