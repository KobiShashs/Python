def add(num1,num2):
    print("The result is:" , num1 + num2)

def main():
    add(1,3)

if __name__ == "__main__":#will solve this module when imported to other program
    print("I'm running as a script!")
    print("value of __name__ variale is: ",__name__)
    main() 
else:
    print("I'm imported!")
    print("value of __name__ variale is: ",__name__)
