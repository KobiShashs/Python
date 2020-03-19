def who_is_missing(file_name):
    COMMA = ","
    missing=""
    with open(r"c:\Python\numbers.txt") as f:
        lines = f.read().splitlines()
   # numbers = (str(lines).split(",[]"))
    my_str = str(lines).replace(',','').replace('[','').replace(']','').replace('\'','')
    my_list = sorted(list(my_str))
    idx = 1;
    for x in my_list:
        if(int(x)==idx):
            idx+=1
            continue
        else:
            print(idx)
            break
 


who_is_missing("c:\Python\numbers.txt")