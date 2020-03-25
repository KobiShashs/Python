class BigThing:
    def __init__(self, something):
        self._something = something

    def size(self):
        if(type(self._something) == int):
            print(self._something)
        else:
            print(len(self._something))

class BigCat(BigThing):
    def __init__(self, something, weight):
        super().__init__(something)
        self._weight = weight

    def size(self):
        if(self._weight > 20):
            print("Very Fat")
        elif (self._weight > 15):
            print("Fat")
        else:
            print("OK")

def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())

    cutie = BigCat("mitzy", 22)
    print(cutie.size())

main()
