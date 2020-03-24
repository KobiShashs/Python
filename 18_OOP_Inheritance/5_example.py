class A:
    def __init__(self):
        self._secret = 12
        
    def print_secret(self):
        print(self._secret)

class B(A):
    pass

def main():
    b = B()
    b.print_secret()

main()