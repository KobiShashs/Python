def city_generator():
    print("START")#will not print, it is a generator function, returns an object
    yield "London"
    yield "Berlin"
    yield "Amsterdam"


city = city_generator()
print(city)