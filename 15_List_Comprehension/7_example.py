import functools

print(max(open(r'c:\Python\names.txt', 'r'), key=len))

print((sum(len(line.replace("\n",'')) for line in open(r'c:\Python\names.txt', 'r').read())))


print(min(open(r'c:\Python\names.txt', 'r'), key=len))

print("***********************")

print([line.replace("\n",'') for line in open(r'c:\Python\names.txt', 'r').readlines() ])

minimum_len = len(min(open(r'c:\Python\names.txt', 'r'), key=len))
print([line.replace("\n",'') for line in open(r'c:\Python\names.txt', 'r').readlines() ])



