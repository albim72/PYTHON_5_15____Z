from abc import ABC,abstractmethod

class Abstrakcja(ABC):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def message(self,info):
        print(f"informacja: {info}")

    @abstractmethod
    def policz_sume(self):
        return self.x+self.y+self.z

    @abstractmethod
    def policz_cos(self):
        pass

class Zwykla(Abstrakcja):

    def policz_sume(self):
        return super().policz_sume()

    def policz_cos(self):
        return (self.x+self.y)*self.z


zw = Zwykla(5,3,5)
print(zw.policz_sume())
print(zw.policz_cos())


