balance = 0
def deposit(amount):
    global balance
    balance += amount
def withdraw(amount):
    global balance
    balance -= amount
def print_balance():
    global balance
    print("Current balance is:", balance)


deposit(100)
deposit(50)
withdraw(20)
print_balance()

#This solution works onlyif we have one account only
