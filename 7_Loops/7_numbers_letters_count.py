def numbers_letters_count(my_str):
    list_res = []
    list_res.append(len(my_str))
    count_digits = 0
    count_letters = 0;
    for str_num in my_str:
        if(str(str_num).isdigit()):
            count_digits+=1;
        if(str(str_num).isalnum()):
            count_letters+=1;
    list_res.append(count_digits)
    list_res.append(count_letters)
    return(list_res)

print(numbers_letters_count("Python 3.6.3"))
#[3, 9]