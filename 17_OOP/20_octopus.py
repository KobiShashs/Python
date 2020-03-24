class Octopus:
    count_animal = 0
    def __init__(self,name="Octavio"):
        self._name = name
        self._age = 32
        Octopus.count_animal+=1

    def set_name(self,name):
        self._name = name

    def get_name(self):
        return self._name

    def birthday_increase(self):
        self._age+=1
    def birthday_decrease(self):
        self._age-=1
    
    def get_age(self):
        return self._age

def main():
    print("-----O1-----")
    o1 = Octopus("Mosh")
    print(o1.get_name())
    o1.set_name("Moshon")
    print(o1.get_name())
    print("-----O2-----")
    o2 = Octopus()
    print(o2.get_name())
    o2.set_name("Octush")
    print(o2.get_name())
    print("---TOTAL_---")
    print(Octopus.count_animal)
    #print(o1.count_animal)
    #print(o2.count_animal)
main()