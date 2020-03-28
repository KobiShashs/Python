# ------------------------Username Custom Exceptions--------------------------------
class UsernameContainsIllegalCharacter (Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        
        return "Your username {0} contains IllegalCharacters, at location: {1}".format(self._username,self.get_fisrt_bad_index(self._username))

    def get_username(self):
        return self._username

    def get_fisrt_bad_index(self,username):
        string_check = "[.@!#$%^&*()<>?/\|}{~:]'"
        idx = 0;
        for x in username:
            if (x in string_check):
                return idx
            else:
                idx+=1

        return -1


class UsernameTooShort (Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your username %s is too short" % self._username

    def get_username(self):
        return self._username


class UsernameTooLong  (Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your username %s is too long" % self._username

    def get_username(self):
        return self._username

# ------------------------Password Custom Exceptions--------------------------------


class PasswordMissingCharacter (Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password %s missing a cetain character" % self._password

    def get_password(self):
        return self._password


class PasswordTooShort (Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password %s is too short" % self._password

    def get_username(self):
        return self._password


class PasswordTooLong  (Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "Your password %s is too long" % self._password

    def get_username(self):
        return self._password


# ------------------------Helper Functions--------------------------------
def is_valid_username(username):
    import re
    string_check = re.compile('[.@_!#$%^&*()<>?/\|}{~:]')
    return ((any(char.isdigit() for char in username)) and
            (any(c.isalpha() for c in username)) and ("_" in username)
            and (string_check.search(username) == None))


def is_valid_password(password):
    # import string library function
    import re
    string_check = re.compile('[.@_!#$%^&*()<>?/\|}{~:]')
    return ((any(x.isupper() for x in password))
            and (any(x.islower() for x in password))
            and (any(char.isdigit() for char in password))
            and (string_check.search(password) != None))

# ------------------------Username Validation--------------------------------

def check_input_username(username):
    try:
        if(not is_valid_username(username)):
            raise UsernameContainsIllegalCharacter(username)
        if (len(username) < 3):
            raise UsernameTooShort(username)
        elif (len(username) > 16):
            raise UsernameTooLong(username)
    except UsernameContainsIllegalCharacter as e:
        print(e.__str__())
    except UsernameTooShort as e:
        print(e.__str__())
    except UsernameTooLong as e:
        print(e.__str__())
    else:
        print("OK")

# ------------------------Password Validation--------------------------------
def check_input_password(password):
    try:
        if (not is_valid_password(password)):
            raise PasswordMissingCharacter(password)
        elif (len(password) < 8):
            raise PasswordTooShort(password)
        elif (len(password) > 40):
            raise PasswordTooLong(password)
    except PasswordMissingCharacter as e:
        print(e.__str__())
    except PasswordTooShort as e:
        print(e.__str__())
    except PasswordTooLong as e:
        print(e.__str__())
    else:
        print("OK")
# ------------------------------------------------------------------------

def check_input(username, password):
    try:
        if(not is_valid_username(username)):
            raise UsernameContainsIllegalCharacter(username)
        if (len(username) < 3):
            raise UsernameTooShort(username)
        elif (len(username) > 16):
            raise UsernameTooLong(username)
        elif (not is_valid_password(password)):
            raise PasswordMissingCharacter(password)
        elif (len(password) < 8):
            raise PasswordTooShort(password)
        elif (len(password) > 40):
            raise PasswordTooLong(password)
    except UsernameContainsIllegalCharacter as e:
        print(e.__str__())
    except UsernameTooShort as e:
        print(e.__str__())
    except UsernameTooLong as e:
        print(e.__str__())
    except PasswordMissingCharacter as e:
        print(e.__str__())
    except PasswordTooShort as e:
        print(e.__str__())
    except PasswordTooLong as e:
        print(e.__str__())
    else:
        print("OK")

def main():
    print("----------------START------------------")
    username = input("Please insert username: ")
    while(not is_valid_username(username)):
        check_input_username(username)
        username = input("Please insert username: ")
    
    password = input("Please insert password: ")
    while(not is_valid_password(password)):
        check_input_password(password)
        password = input("Please insert password: ")
    print("-----------------END-------------------")


if __name__ == "__main__":
    main()

