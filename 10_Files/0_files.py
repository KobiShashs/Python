my_file = open("c:\Python\players.txt","r")
for line in my_file:
    print(str(line))
    if("Messy" in line):
        print("Best player in the world!")
my_file.close()