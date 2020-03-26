NOT_EXISTING_FILE = "moshe_file.txt"
EXSITING_FILE="c:\Python\players.txt"
def get_file_line_num(file_name):
    try:
         f = open(file_name)
    except IOError:
        print("IO Error with file: ", file_name)
    else:
        print("Number of lines in file: ", len(f.readlines()))
        f.close()

get_file_line_num(EXSITING_FILE)
get_file_line_num(NOT_EXISTING_FILE)