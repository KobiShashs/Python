def print_welcome_prompt():
    HANGMAN_ASCII_ART = '''  
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/ '''

    print(HANGMAN_ASCII_ART)

def print_hangman(num_of_tries):
    pic1 = '''    x-------x'''
    pic2 = '''    x-------x
    |
    |
    |
    |
    |'''
    pic3 = '''    x-------x
    |       |
    |       0
    |
    |
    |'''
    pic4 = '''    x-------x
    |       |
    |       0
    |       |
    |
    |'''
    pic5 = '''    x-------x
    |       |
    |       0
    |      /|\\
    |
    |'''
    pic6 = '''    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |'''
    pic7 = '''    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |'''

    HANGMAN_PHOTOS = {"pic_1":pic1,"pic_2":pic2,"pic_3":pic3,
                        "pic_4":pic4,"pic_5":pic5,"pic_6":pic6,"pic_7":pic7}
    
    if(num_of_tries==1):
        print(HANGMAN_PHOTOS["pic_1"])
    elif(num_of_tries==2):
        print(HANGMAN_PHOTOS["pic_2"])
    elif(num_of_tries==3):
        print(HANGMAN_PHOTOS["pic_3"])
    elif(num_of_tries==4):
        print(HANGMAN_PHOTOS["pic_4"])
    elif(num_of_tries==5):
        print(HANGMAN_PHOTOS["pic_5"])
    elif(num_of_tries==6):
        print(HANGMAN_PHOTOS["pic_6"])
    elif(num_of_tries==7):
        print(HANGMAN_PHOTOS["pic_7"])

