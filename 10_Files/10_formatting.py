cd_details = {"song":"Hello","artist":"Lionel Richie","year":1983}
my_file = open(r"C:\Python\my_song.txt","w")
for key, value in cd_details.items():
    my_file.write("%s: %s \n" % (key,value))
my_file.close()

f = open(r"C:\Python\my_song.txt","r")
data = f.read();
lines = data.split("\n")
items=[]
for element in lines:
    items.append(element.split(":"))
my_dict = {}
for item in items:
   # my_dict[item[0]]=item[1]
    print(item)
f.close()
print(my_dict)