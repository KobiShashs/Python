class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def print_balance(self):
        print("Current balance is:", self.balance)
def main():
    ran = BankAccount()
    ran.deposit(1200)
    ran.withdraw(200)
    ran.print_balance()
main()