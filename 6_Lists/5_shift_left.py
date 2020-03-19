def shift_left(my_list):
    tmp =my_list[0]
    my_list[0]=my_list[1]
    my_list[1]=my_list[2]
    my_list[2]=tmp
    return my_list

print(shift_left([0,1,2]))
print(shift_left([2.0,1,'moshe']))