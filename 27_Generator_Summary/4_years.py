def gen_years(start=2019):
    #<yield>
    while True:
        yield start
        start+=1

years = gen_years()
print(next(years))
print(next(years))
print(next(years))