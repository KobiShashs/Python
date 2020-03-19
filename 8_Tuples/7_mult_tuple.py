def mult_tuple(tuple1, tuple2):
    res = []
    len1 = len(tuple1)
    for i in range(0, len1, 1):
        len2 = len(tuple2)
        for j in range(0, len2, 1):
            my_tuple = tuple1[i], tuple2[j]
            res.append(my_tuple)

    len1 = len(tuple2)
    for i in range(0, len1, 1):
        len2 = len(tuple1)
        for j in range(0, len2, 1):
            my_tuple = tuple2[i], tuple1[j]
            res.append(my_tuple)
    return res

first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))
