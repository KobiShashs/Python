def gen_secs():
    time = 0
    while True:
        yield time%60
        time+=1

seconds = gen_secs()
print(next(seconds))
print(next(seconds))
print(next(seconds))
print(next(seconds))
print(next(seconds))
print(next(seconds))
print(next(seconds))
print(next(seconds))