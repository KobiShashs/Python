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


class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)


class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)


class Skunk(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)


class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)


class Dragon(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)


def main():
    d1 = Dog("Brownie", 10)
    c1 = Cat("Zelda", 3)
    s1 = Skunk("Stinky", 0)
    u1 = Unicorn("Keith", 10)
    dr1 = Dragon("Lizzy", 1450)
    zoo_list = [d1, c1, s1, u1, dr1]

    for animal in zoo_list:
        print("Type : {} , Name : {}".format(type(animal), animal.get_name()))
        while animal.is_hungry():
            animal.feed()


main()
