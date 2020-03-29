with open("capitals.txt") as file:
    single_line_gen = (line for line in file)

with open("capitals.txt") as file:
    single_line_gen = (line for line in file)
    print(next(single_line_gen))
    print(next(single_line_gen))
    print(next(single_line_gen))
    print(next(single_line_gen))


with open("capitals.txt") as file:
    single_line_gen = (line for line in file)
    capitals_and_cities = (l.replace("\n", ("")).split(",") for l in single_line_gen)

with open("capitals.txt") as file:
    single_line_gen = (line for line in file)
    capitals_and_cities = (l.replace("\n", ("")).split(",") for l in single_line_gen)
    print(next(capitals_and_cities))
    print(next(capitals_and_cities))
    print(next(capitals_and_cities))
    print(next(capitals_and_cities))

