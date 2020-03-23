import functools
def add(x, y):
    return x + y
shopping_list = []
print(functools.reduce(add, shopping_list,0))# Improtant
