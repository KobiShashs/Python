def squared_numbers(start, stop):
    my_list = []
    i=0
    while(stop-start>=0):
        my_list.append(str(int(start)**2))
        start+=1

    print(my_list)


squared_numbers(4, 8)
#[16, 25, 36, 49, 64]
squared_numbers(-3, 3)
#[9, 4, 1, 0, 1, 4, 9]
