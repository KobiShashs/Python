class BankAccount:

    def __init__(self):
        self.balance = 0

    def greet(self,name):
        print ("Welcome",name)

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

def main():

    kobis_account = BankAccount()
    kobis_account.greet("Kobi")
    kobis_account.deposite(1500)
    print(kobis_account.balance)
    
    rogers_account = BankAccount()
    rogers_account.greet("Roger")
    rogers_account.deposite(1399)
    print(rogers_account.balance)
    
    rogers_account.withdraw(249)
    print(rogers_account.balance)

if __name__ == "__main__":
    main()