#print all primary numbers in range 0-10^10

def is_prime(n):
    import math
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# Don't try to run this at home!!! - lazy evaluation
primre_generator = (n for n in range (10**10) if is_prime(n))
for prime_number in primre_generator:
    print(prime_number)