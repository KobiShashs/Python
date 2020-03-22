def square(num):
    return num ** 2


list_of_numbers = [2, 3, 4, 5, 6]
new_list = []
for number in list_of_numbers:
    new_list.append(square(number))
print(new_list)

print("*********************************************************")

list_of_numbers = [2, 3, 4, 5, 6]
new_list = []
new_list =  [square(i) for i in list_of_numbers]
print(new_list)

print("*********************************************************")

list_of_numbers = [2, 3, 4, 5, 6]
new_list = list(map(square,list_of_numbers))
print(new_list)