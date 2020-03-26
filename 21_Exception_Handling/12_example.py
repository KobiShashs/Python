NOT_EXISTING_FILE = "moshe_file.txt"
EXSITING_FILE="c:\Python\players.txt"
def read_file(file_name):
    try:
         print("__CONTENT_START__")
         f = open(file_name)
    except IOError:
        print("__NO_SUCH_FILE__")
    else:
        print(f.read())
        f.close()
    finally:
        print("__CONTENT_END__")


print(read_file(EXSITING_FILE))
print("----")
print(read_file(NOT_EXISTING_FILE))