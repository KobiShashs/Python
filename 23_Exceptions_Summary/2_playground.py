def is_valid_username(username):
    import re
    string_check = "[.@!#$%^&*()<>?/\|}{~:]'"
    for x in username:
            if (x in string_check):
                return False;
    return ((any(char.isdigit() for char in username)) and
            (any(c.isalpha() for c in username)) and ("_" in username))



def get_fisrt_bad_index(username):
        string_check = "[.@!#$%^&*()<>?/\|}{~:]'"
        idx = 0;
        for x in username:
            if (x in string_check):
                return idx
            else:
                idx+=1

        return -1



print(is_valid_username("A_a1."))
#print(get_fisrt_bad_index("A_a1."))
print(is_valid_username("A_1"))
#print(get_fisrt_bad_index("A_1"))