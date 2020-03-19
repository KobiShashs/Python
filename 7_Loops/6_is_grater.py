def is_greater(my_list, n):
    res = []
    for element in my_list:
        if(int(element)>n):
            res.append(element)
    return res



result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)
#[30, 60]