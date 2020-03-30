def gen_minutes():
    time = 0
    while True:
        yield time%60
        time+=1

minutes = gen_minutes()
print(next(minutes))
print(next(minutes))
print(next(minutes))
print(next(minutes))
print(next(minutes))
