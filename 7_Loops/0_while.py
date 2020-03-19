import math
def squared_numbers(start, stop):
    mylist = []
    pattern=" , "
    while((stop-start)>=0):
        if(stop-start==0):
            pattern=""
        print(str(math.pow(start,2))+pattern,end="")
        start+=1
    print()

squared_numbers(4, 8)
#[16, 25, 36, 49, 64]
squared_numbers(-3, 3)
#[9, 4, 1, 0, 1, 4, 9]