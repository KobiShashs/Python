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

    first_acc = BankAccount()
    second_acc = BankAccount()

    first_acc.bank_name = "MoshikoBank"

    print(first_acc.bank_name)#Will change
    print(second_acc.bank_name)#Will not change

if __name__ == "__main__":
    main()
