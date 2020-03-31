my_list = [2, 1]

first_iterator = iter(my_list)
addition = next(first_iterator) + next(first_iterator)
print(addition)

print("-------")

second_iterator = iter(my_list) #Right
multipication = next(second_iterator) * next(second_iterator)
print(multipication)
