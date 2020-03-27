class UnderAge(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "Your age %d is under 18. sorry :(" % self._age

    def get_arg(self):
        return self._age


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e.__str__())
    else:
        print("You should send an invite to " + name)

send_invitation("Moshe",20)
send_invitation("David",17)


