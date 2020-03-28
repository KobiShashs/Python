def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    primre_generator = (n for n in range (n,n ** 2) if is_prime(n))
    return(next(primre_generator))



print(first_prime_over(1000000))
#1000003