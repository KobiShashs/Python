import functools
def double_it(char):
    return char+char


def double_letter(my_str):
    return "".join(str(x) for x in  list(map(double_it,my_str)))


print(double_letter("python"))
print(double_letter("we are the champions!"))
