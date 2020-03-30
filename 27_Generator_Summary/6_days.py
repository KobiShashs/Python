def gen_days(month, leap_year=True):
    num_of_days = 0
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        num_of_days=31
    elif(month==4 or month==6 or month==9 or month==11):
        num_of_days=30
    elif(month==2):
        if(leap_year):
            num_of_days=29
        else:
            num_of_days=28

    time = 0

    while True:
        yield (time%num_of_days +1)



days =  gen_days(2, True)
print(next(days))