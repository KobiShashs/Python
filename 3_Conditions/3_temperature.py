temperature = input("Please insert temperatur: ")
print(temperature)
unit = temperature[-1]
temperature = temperature[:-1:]
print(temperature)
print(unit)
if(unit == "F"):
    val = (5*float(temperature)-160)/9
    print(str(val).__add__("C"))
elif(unit == "C"):
    val = (9*float(temperature) + (32*5))/5
    print(str(val)+"F")
else:
    print("Didn't got you...")
