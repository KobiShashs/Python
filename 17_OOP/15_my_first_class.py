class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposite(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
    
    def print_blance(self):
        print("Current Balance is", self._balance)

def main():

    newbie_acc = BankAccount()
    newbie_acc.print_blance()#AttributeError: 'BankAccount' object has no attribute 'balance'
    newbie_acc.deposite(500)
    print(newbie_acc.balance)
    newbie_acc.print_blance()
    newbie_acc.balance=0 #Too dangerous!
    newbie_acc.print_blance()

    
    legacy_acc = BankAccount(600)
    legacy_acc.print_blance()
    legacy_acc.deposite(500)
    print(legacy_acc.balance)
    legacy_acc.print_blance()
    legacy_acc.balance=0 #Too dangerous!
    legacy_acc.print_blance()

if __name__ == "__main__":
    main()
