def remainder(base, divide_by=2, show_greeting=True):
    print("base",base)
    print("divide_by",divide_by)
    print("show_greeting",show_greeting)
    if show_greeting:
        print("Welcome to my function")
    
    print(base % divide_by)

remainder(3,2,True)
remainder(3,2)
remainder(3)