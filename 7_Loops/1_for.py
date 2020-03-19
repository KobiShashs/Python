def is_greater(my_list, n):
    res = []
    for num in my_list:
        if(not num<=n):
            res.append(num)
    return res

print(is_greater([1, 30, 25, 60, 27, 28], 28))
# actual: ['3', '0', '6', '0']
# expected: [30, 60]