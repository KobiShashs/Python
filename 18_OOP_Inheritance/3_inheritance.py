class Animal:
    def __init__(self,name):
        self._name = name
        self._hunger = 0
        self._fun = 0
    
    def play(self):
        self._fun+=1
    
    def eat(self):
        if(self._hunger >0):
            self._hunger-=1
    
    def go_to_toilet(self):
        self._hunger +=1

class Dog(Animal):
     def __init__(self,name,fun_color):
        Animal.__init__(self,name)#can be replaced by super() call
        self._fun_color = fun_color

     def go_for_a_walk(self):
        self._fun +=2
        print("Waff waff! My fun level is rising, and its: ",self._fun)

def main():
    duly = Dog("Duly","Black")
    duly.play()
    duly.eat()
    duly.go_for_a_walk()

main()