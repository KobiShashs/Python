def city_generator():
    print("START")#will not print, it is a generator function, returns an object
    yield "London"
    yield "Berlin"
    yield "Amsterdam"


city_loop_genx = city_generator()
for city in city_loop_genx:
    print(city)
