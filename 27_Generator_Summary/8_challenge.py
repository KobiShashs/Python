def gen_secs():
    time = 0
    while True:
        yield time%60
        time+=1

def gen_minutes():
    time = 0
    while True:
        yield time%60
        time+=1


def gen_hours():
    time = 0
    while True:
        yield time%24
        time+=1

def gen_time():
    seconds = gen_secs()
    minutes = gen_minutes()
    hours = gen_hours()
    hh = next(hours)
    mm = next(minutes)
    ss = next(seconds)
    
    while True:
        res = "%02d:%02d:%02d"% ((hh),(mm),(ss))
        ss+=1
        yield res

        if(ss==60):
            mm+=1
            ss=0
        
        if(mm==60):
            hh+=1
            mm=0
            ss=0

        if(hh==24):
            hh=0
            mm=0
            ss=0

        

def gen_years(start=2019):
    #<yield>
    while True:
        yield start
        start+=1

def gen_months():
    time = 0
    while True:
        yield (time%12 + 1)
        time+=1

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


def gen_date():
    time = gen_time()
    years = gen_years()
    months = gen_months()
    days = gen_days(next(months))
    yyyy = next(years)
    mm = next(months)
    dd = next(days)

    count=0
    while True:
        res = (str(dd)+"/"+str(mm)+"/"+str(yyyy)+" ")+next(time)
        count+=1
        yield res

        if(count==86400):
            dd+=1
            count=0

    

my_date = gen_date()
for i in range(0,1000000):
    print(next(my_date))
