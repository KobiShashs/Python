def last_early(my_str):
    my_str = str(my_str).casefold()
    # if(str(my_str[-1]).casefold() in str(my_str[0:len(my_str)-1]).casefold()):
    if(my_str[-1] in my_str[0:len(my_str)-1]):
        print("True")
    else:
        print("False")


last_early("happy birthday")
# True
last_early("best of luck")
# False
last_early("Wow")
# True
last_early("X")
# False
