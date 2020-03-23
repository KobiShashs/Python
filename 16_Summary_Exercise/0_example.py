import functools

print("Longest Name:")
print(max(open(r'c:\Python\names.txt', 'r'), key=len))

print("total lenghts:")
print((sum(len(line.replace("\n",'')) for line in open(r'c:\Python\names.txt', 'r').read())))

print("minimal lenght string is:")
print(min(open(r'c:\Python\names.txt', 'r'), key=len))




