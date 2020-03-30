def gen_hours():
    time = 0
    while True:
        yield time%24
        time+=1

hours = gen_hours()
print(next(hours))
print(next(hours))
print(next(hours))
print(next(hours))
print(next(hours))
