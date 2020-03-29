def my_gen(x, y):
    x += 1
    while x < y:
        yield x
        
for i in my_gen(6, 9):
    print(i)