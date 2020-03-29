
def get_fibo():
    a1 = 0
    a2 = 1
    
    while True:
        yield a1
        a2 = a2 + a1
        a1 = a2-a1
   
fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))