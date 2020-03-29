import random

#Generator that generates 4 random numbers respresenting dice rolls.
cube_game  = (random.randint(1,6) for i in range(4))
total = 0
for num in cube_game:
    print(num)
    total+=num

print("total",total)
