iterable = ["a","b","c"]


# standatrt for loop
for item in iterable:
    print("do something")

print("-------------")
#behind the scene 

# Create an iterator object from that iterable
iter_obj = iter(iterable)
# Infinite loop
while True:
    try:
        #Get the next item
        item = next(iter_obj)
        #Do somwthing with the element
        print("do something")
    except StopIteration:
        #If StopIteration is raised, break the loop
        break

