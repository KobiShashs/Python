class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def print_blance(self):
        print("Current Balance is", self.balance)

def main():

    newbie_acc = BankAccount()
    newbie_acc.print_blance()
    
    legacy_acc = BankAccount(600)
    legacy_acc.print_blance()

if __name__ == "__main__":
    main()
