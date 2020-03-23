class Octopus:
    def __init__(self):
        self.name = "Octavio"
        self.age = 32

    def birthday_increase(self):
        self.age+=1
    def birthday_decrease(self):
        self.age-=1
    
    def get_age(self):
        return self.age

def main():
    print("-----O1-----")
    o1 = Octopus()
    print(o1.get_age())
    o1.birthday_increase()
    print(o1.get_age())
    print("-----O2-----")
    o2 = Octopus()
    print(o2.get_age())
    o2.birthday_decrease()
    print(o2.get_age())
main()