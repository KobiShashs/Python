def seven_boom(end_number):
    res = []
    for num in range(0,end_number+1,1):
        if((int(num)%7==0) or ("7" in str(num))):
            res.append("Boom")
        else:
            res.append(num)
    return res

print(seven_boom(17))
#['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']