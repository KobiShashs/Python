class BankAccount:
    def greet(self,name):
        print ("Welcome",name)

def main():
    kobis_account = BankAccount()
    kobis_account.greet("Kobi")
    
    rogers_account = BankAccount()
    rogers_account.greet("Roger")


if __name__ == "__main__":
    main()