def facorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact*i
    return fact

print(facorial(5))
print(facorial(-5))# Not valid yes?