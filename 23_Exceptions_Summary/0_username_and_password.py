# ------------------------Username Custom Exceptions--------------------------------
class UsernameContainsIllegalCharacter (Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "Your username %s contains IllegalCharacters" % self._username

    def get_username(self):
        return self._username


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
    return (
            (any(char.isdigit() for char in username)) 
            and
            (any(c.isalpha() for c in username)) 
            and 
            ("_" in username)
        )


def is_valid_password(password):
    # import string library function
    import re
    string_check = re.compile('[.@_!#$%^&*()<>?/\|}{~:]')
    return ((any(x.isupper() for x in password))
            and (any(x.islower() for x in password))
            and (any(char.isdigit() for char in password))
            and (string_check.search(password) != None))


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


check_input("1", "2")
check_input("0123456789ABCDEFG", "2")
check_input("A_a1.", "12345678")
check_input("A_1", "2")
check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")