class BankAccount:

    def __init__(self):
        self.balance = 0

    def greet(self, name):
        print("Welcome", name)
    
    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def print_blance(self):
        print("Current Balance is", self.balance)

def main():

    kobis_account = BankAccount()
    kobis_account.greet("Kobi")
    kobis_account.deposite(400)
    kobis_account.print_blance()
    
    rogers_account = BankAccount()
    rogers_account.greet("Roger")
    rogers_account.deposite(20)
    rogers_account.print_blance()

if __name__ == "__main__":
    main()
