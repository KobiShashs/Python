# ------------------------Username Custom Exceptions--------------------------------
class UsernameContainsIllegalCharacter (Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):

        return "Your username {0} contains IllegalCharacters, at location: {1}".format(self._username, self.get_fisrt_bad_index(self._username))

    def get_username(self):
        return self._username

    def get_fisrt_bad_index(self, username):
        string_check = "[.@!#$%^&*()<>?/\|}{~:]'"
        idx = 0
        for x in username:
            if (x in string_check):
                return idx
            else:
                idx += 1

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


class PasswordMissingCharacterUppercase (PasswordMissingCharacter):
    def __init__(self, password):
         super().__init__(password)
    def __str__(self):
        return "Your password %s missing a character (Uppercase)" % self._password

    def get_password(self):
        return self._password


class PasswordMissingCharacterLowercase (PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def __str__(self):
        return "Your password %s missing a character (Lowercase)" % self._password

    def get_password(self):
        return self._password


class PasswordMissingCharacterDigit (PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def __str__(self):
        return "Your password %s missing a character (Digit)" % self._password

    def get_password(self):
        return self._password


class PasswordMissingCharacterSpecial (PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def __str__(self):
        return "Your password %s missing a character (Special)" % self._password

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
    string_check = "[.@!#$%^&*()<>?/\|}{~:]'"
    for x in username:
        if (x in string_check):
            return False
    return ((any(char.isdigit() for char in username)) and
            (any(c.isalpha() for c in username)) and ("_" in username))


def is_valid_password(password):
    # import string library function
    import re
    string_check = re.compile('[.@_!#$%^&*()<>?/\|}{~:]')
    return ((any(x.isupper() for x in password))
            and (any(x.islower() for x in password))
            and (any(char.isdigit() for char in password))
            and (string_check.search(password) != None))


def is_password_missing_uppercase_letter(password):
    return not any(x.isupper() for x in password)


def is_password_missing_lowercase_letter(password):
    return not any(x.islower() for x in password)


def is_password_missing_digit_letter(password):
    return not any(char.isdigit() for char in password)


def is_password_missing_special_letter(password):
    # import string library function
    import re
    string_check = re.compile('[.@_!#$%^&*()<>?/\|}{~:]')
    return string_check.search(password) == None
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
            if(is_password_missing_uppercase_letter(password)):
                raise PasswordMissingCharacterUppercase(password)
            elif(is_password_missing_lowercase_letter(password)):
                raise PasswordMissingCharacterLowercase(password)
            elif(is_password_missing_digit_letter(password)):
                raise PasswordMissingCharacterDigit(password)
            elif(is_password_missing_special_letter(password)):
                raise PasswordMissingCharacterSpecial(password)
        elif (len(password) < 8):
            raise PasswordTooShort(password)
        elif (len(password) > 40):
            raise PasswordTooLong(password)

    except PasswordMissingCharacterUppercase as e:
        print(e.__str__())
    except PasswordMissingCharacterLowercase as e:
        print(e.__str__())
    except PasswordMissingCharacterDigit as e:
        print(e.__str__())
    except PasswordMissingCharacterSpecial as e:
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
            if(is_password_missing_uppercase_letter(password)):
                raise PasswordMissingCharacterUppercase(password)
            elif(is_password_missing_lowercase_letter(password)):
                raise PasswordMissingCharacterLowercase(password)
            elif(is_password_missing_digit_letter(password)):
                raise PasswordMissingCharacterDigit(password)
            elif(is_password_missing_special_letter(password)):
                raise PasswordMissingCharacterSpecial(password)
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
    except PasswordMissingCharacterUppercase as e:
        print(e.__str__())
    except PasswordMissingCharacterLowercase as e:
        print(e.__str__())
    except PasswordMissingCharacterDigit as e:
        print(e.__str__())
    except PasswordMissingCharacterSpecial as e:
        print(e.__str__())
    except PasswordTooShort as e:
        print(e.__str__())
    except PasswordTooLong as e:
        print(e.__str__())
    else:
        print("OK")


def main():
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
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
