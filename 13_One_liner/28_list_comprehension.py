list1 = [1,2,3]
list2 = [5,6,7]

mult_list =[]
for x in list1:
    for y in list2:
        mult_list.append(x*y)
print(mult_list)



mult_list = [x*y for x in list1 for y in list2]
print(mult_list)