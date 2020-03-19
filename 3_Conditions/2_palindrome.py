str1 = "Borrow or rob"
origin = str1.replace(" ", "").lower()
opposite = str1[::-1].replace(" ", "").lower()
print("origin    : ", origin)
print("opposite  : ", opposite)
if(origin == opposite):
    print("Palindrome")
else:
    print("Not a Palindrome")
