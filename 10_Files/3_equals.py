def are_files_equal(file1, file2):
    import filecmp
    return filecmp.cmp(file1, file2) 
print(are_files_equal(r"c:\Python\players1.txt", r"c:\Python\players2.txt"))