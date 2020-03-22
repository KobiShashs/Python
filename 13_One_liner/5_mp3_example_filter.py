# List of file names
my_files = ["Great Spirit.mp3","I need you.mp3","London 2018.docx",
"my selfie.jpeg","This Light Between Us.mp3"]

# Filter mp3 files using the "filter" function
def is_mp3_file(file_name):
    return file_name.endswith(".mp3")

print(list(filter(is_mp3_file,my_files)))

