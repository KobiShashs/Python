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


my_time = gen_time()
print(next(my_time))
print(next(my_time))
print(next(my_time))
