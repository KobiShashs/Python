class Animal:
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = 0

    def get_name(self):
        return self._name

    def is_hungry(self):
        return (self._hunger > 0)

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    d1 = Dog("Brownie", 10)
    c1 = Cat("Zelda", 3)
    s1 = Skunk("Stinky", 0)
    u1 = Unicorn("Keith", 10)
    dr1 = Dragon("Lizzy", 1450)
    zoo_list = [d1, c1, s1, u1, dr1]

    for animal in zoo_list:
        print("Type : {} , Name : {}".format(type(animal), animal.get_name()))
        animal.talk()
        if(isinstance(animal, Dog)):
            animal.fetch_stick()
        elif(isinstance(animal, Cat)):
            animal.chase_laser()
        elif(isinstance(animal, Skunk)):
            animal.stink()
        elif(isinstance(animal, Unicorn)):
            animal.sing()
        elif(isinstance(animal, Dragon)):
            animal.breath_fire()

        while animal.is_hungry():
            animal.feed()


main()
