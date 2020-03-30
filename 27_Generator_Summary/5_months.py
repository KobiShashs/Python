def gen_months():
    time = 0
    while True:
        yield (time%12 + 1)
        time+=1

months = gen_months()
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))
print(next(months))