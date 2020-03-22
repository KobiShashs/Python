# List of file names
my_files = ["Great Spirit.mp3","I need you.mp3","London 2018.docx",
"my selfie.jpeg","This Light Between Us.mp3"]

# Filter only mp3 using a standart "for" loop
mp3_list = []
for file in my_files:
    if file.endswith(".mp3"):
        mp3_list.append(file)
print(mp3_list)



def func(x):
    return x % 2 != 0
print(list(filter(func, range(10))))