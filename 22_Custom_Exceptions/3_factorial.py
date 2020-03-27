class FactorialArgumentError(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Provided argument %s is not a posotive integer." % self._arg

    def get_arg(self):
        return self._arg

def facorial(n):
    if( not isinstance(n,int) or n<0):
       raise FactorialArgumentError(n)
    else:
        fact = 1
        for i in range(n,0,-1):
            fact = fact*i
        return fact

print(facorial(5))
print(facorial(-5))# But it returns None and not an integer, what can be wrong?