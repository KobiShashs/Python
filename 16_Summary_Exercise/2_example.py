print("Sorted list by lenght")
print(sorted([line.replace("\n", '') for line in open(
    r'c:\Python\names.txt', 'r').readlines()], key=len))
minimum_len = int(input("Please insert lenght: "))
print("minimum_len", minimum_len)
print("filter list by minimal lenght")
print(list(filter(lambda x: len(x) == minimum_len, sorted([line.replace(
    "\n", '') for line in open(r'c:\Python\names.txt', 'r').readlines()], key=len))))
