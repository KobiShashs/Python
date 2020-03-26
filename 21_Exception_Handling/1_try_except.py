num1 = int(input("Enter 1st number: "))#5   
num2 = int(input("Enter 2nd number "))#0
try:
    print("The result is : " + str(num1/num2)) #ZeroDivisionError: division by zero
except:
    print("Sorry, you cannot divide the provided input.")
    
