def last_print(file_path):
    num_lines = input("how many lines? ")
    my_file = open(str(file_path),"r")
    lines = my_file.readlines()
    i=0
    for line in reversed(lines):
        if(i<int(num_lines)):
            i+=1
            print(line)
        else:
            break

def rev_print(file_path):
    my_file = open(str(file_path),"r")
    for line in my_file:
        print(str(line)[::-1])

def sort_print(file_path):
    huge_list = []
    with open(str(file_path), "r") as f:
        huge_list = f.read().split()
    print(sorted(huge_list))
    f.close()


def print_from_file_by_action(file_path,action):
    if(action=="sort"):
        sort_print(file_path)
    elif(action=="rev"):
        rev_print(file_path)
    elif(action=="last"):
        last_print(file_path)
    else:
        print("Not Support action")



print_from_file_by_action("c:\Python\song.txt","sort")
print("*****************************")
print_from_file_by_action("c:\Python\song.txt","rev")
print("*****************************")
print_from_file_by_action("c:\Python\song.txt","last")

