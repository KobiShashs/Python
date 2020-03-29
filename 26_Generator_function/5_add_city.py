def city_generator():
    print("Starting")
    yield "London"
    yield "Berlin"
    yield "Amsterdam"
    

def add_jerusalem_generator():
    yield from city_generator()
    yield "Jerusalem"

patriot = add_jerusalem_generator()
print(next(patriot))
print(next(patriot))
print(next(patriot))
print(next(patriot))