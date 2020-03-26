num1 = int(input("Enter 1st number: "))#5   
num2 = int(input("Enter 2nd number "))#text
try:
    print("The result is : " + str(num1/num2)) #ValueError: invalid literal for int() with base 10: 'text'
except:
    print("Sorry, you cannot divide the provided input.")
    
