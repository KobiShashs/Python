for num in range(1, 20):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if(num % 5 != 0 and num % 3 != 0):
        string = string + str(num)
    print(string)

print("*********************************************************")

print("\n".join(["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, 20)]))
