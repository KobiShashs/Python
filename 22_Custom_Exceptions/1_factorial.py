def facorial(n):
    if(n<0):
        print("Factorial expects non-negative integers..")
    else:
        fact = 1
        for i in range(n,0,-1):
            fact = fact*i
        return fact

print(facorial(5))
print(facorial(-5))# But it returns None and not an integer, what can be wrong?