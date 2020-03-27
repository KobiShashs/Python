import re
string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


def contains_one_special_char(password):
    if(string_check.search(password) == None):
        print("String does not contain Special Characters.")

    else:
        print("String contains Special Characters.")


# contains_one_special_char("aaaaaa")
# contains_one_special_char("aaaaaa")
contains_one_special_char("4BCD3F6h1jk1mn0p")
contains_one_special_char("aaaa!aa")
