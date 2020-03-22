def combine_coins(coin, numbers):
    output = ""
    for num in numbers:
        output += coin + str(num) + ', '
    # Ignore the last comma.
    return output[:-2]

print(combine_coins('$', range(5)))

print("*********************************************************")

def combine_coins2(coin, numbers):
    print(("".join(coin+str(i)+", " for i in numbers))[:-2])

combine_coins2('$', range(5))


print("*********************************************************")

def combine_coins3(coin, numbers):
    return ', '.join(map(lambda s,n:s+str(n),[coin for i in numbers],numbers))


print(combine_coins3('$', range(5)))