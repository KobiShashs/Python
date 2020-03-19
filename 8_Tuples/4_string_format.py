fruit = "grapes"
drink = "wine"

print( "The basket contains " + fruit + " and " + drink + ".")
print("The basket contains %s and %s." % (fruit, drink))

bottles_num, drink = 3, "wine"
print("The basket contains %d bottles of %s." % (bottles_num, drink))

basket_content = 3, "wine"
print("The basket contains %d bottles of %s." % basket_content)