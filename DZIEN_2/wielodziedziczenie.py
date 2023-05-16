from abc import ABC, abstractmethod

class Basic:
    def __init__(self,a):
        self.a = a

    def abc(self):
        print("takietam")

class Second:
    def __init__(self,b):
        self.b = b

    def abc(self):
        print("bla bla")

class Ekstra:
    def __init__(self):
        self.info = "to jest dodatkowa klasa"


class Multi(Second,Basic,Ekstra):
    def __init__(self, a, b, c):
        Basic.__init__(self,a)
        Second.__init__(self,b)
        Ekstra.__init__(self)
        self.c=c
    def __repr__(self):
        return f"a={self.a}, b={self.b}, c={self.c}"

mt = Multi(4,8,2)
print(mt)
print(mt.info)
mt.abc()

# class Moja(ABC):
#     pass
#
# class DrugaA(ABC, Moja):
#     pass



