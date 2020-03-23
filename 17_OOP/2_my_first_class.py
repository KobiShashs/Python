class BankAccount:
    def greet(self,name):
        print ("Welcome",name)

def main():
    kobis_account = BankAccount()
    print(kobis_account)
    
    rogers_account = BankAccount()
    print(rogers_account)


if __name__ == "__main__":
    main()