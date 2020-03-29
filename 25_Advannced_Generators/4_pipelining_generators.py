#integers (1-10) ----> squared(x^2) ----> negated(x*(-1))

integers = (i for i in range(1,11))
squared = (x * x for x in integers)
negated = (-y for y in squared)
for num in negated:
    print(num)