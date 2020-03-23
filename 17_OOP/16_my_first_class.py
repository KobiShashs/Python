class BankAccount:

    bank_name = "PayPy"
    def __init__(self, balance=0):
        self._balance = balance

    def deposite(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
    
    def print_blance(self):
        print("Current Balance is", self._balance)

def main():

    print(BankAccount.bank_name)

    newbie_acc = BankAccount()
    newbie_acc.print_blance()
    print(newbie_acc.bank_name)

    BankAccount.bank_name = "MosheBank" # change class variable value
    
    legacy_acc = BankAccount(600)
    legacy_acc.print_blance()
    print(legacy_acc.bank_name)

if __name__ == "__main__":
    main()
