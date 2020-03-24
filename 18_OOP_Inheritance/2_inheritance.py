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
        Animal.__init__(self,name)
        self._fun_color = fun_color