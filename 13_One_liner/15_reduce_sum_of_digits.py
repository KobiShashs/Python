import functools


def add(x, y):
    return int(x)+int(y)

def sum_of_digits(number):
    return functools.reduce(add, [int(d) for d in str(number)])





print(sum_of_digits(104))