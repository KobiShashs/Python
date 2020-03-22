list_of_tuples = [(2,2),(3,4),(4,1),(1,3)]

print(list_of_tuples)
print(sorted(list_of_tuples))
print(sorted(list_of_tuples,key=lambda x: x[0]))
print(sorted(list_of_tuples,key=lambda x: x[1]))

