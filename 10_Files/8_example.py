def copy_file_content(source, destination):
    import shutil
    shutil.copy(str(source), str(destination))

copy_file_content("c:\Python\copy.txt", "c:\Python\paste.txt")