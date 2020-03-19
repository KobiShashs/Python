def arrow(my_char, max_length):
    for i in range(0,max_length+1,1):
        for j in range(0,i,1):
            print(my_char+" ",end =" ")
        print()
    for i in range(max_length,0,-1):
        for j in range(1,i,1):
            print(my_char+" ",end =" ")
        print()

print(arrow('*', 5))
#*
#* *
#* * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *