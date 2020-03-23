
def is_divide_by_4(num):
    return num%4==0

def four_dividers(number):
    print(list(filter(is_divide_by_4,range(1,number))))

print(four_dividers(9))
print(four_dividers(3))