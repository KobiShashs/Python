import functools


def add(x, y):
    return x+y


shopping_list = [200, 120, 330, 50]

print(functools.reduce(add, shopping_list))
