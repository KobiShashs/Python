import random

total = 0
for i in range(4):
    cube_num = random.randint(1,6)
    print(i,cube_num)
    total+= cube_num

print("total",total)
