class Trash:
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Trash)

    def __init__(self,x,y):
        self.x=x
        self.y=y

t = Trash(3,6)
print(t)
print(t.x)

print("__________________________________________________")

class Kwadrat:
    def __init__(self,bok):
        self.bok = bok

    @property
    def pole(self):
        return self.bok**2

class Prostokat:
    def __new__(cls,a:float,b:float):
        if a==b:
            return Kwadrat(bok=a)
        return object.__new__(Prostokat)

    def __init__(self,a:float,b:float):
        self.a = a
        self.b = b

    @property
    def pole(self):
        return self.a*self.b

r1 = Prostokat(4,7)
r2 = Prostokat(5,5)

print(type(r1))
print(type(r2))                        

print(f"Pole figury: {r1.__class__.__name__} wynosi: {r1.pole}")
print(f"Pole figury: {r2.__class__.__name__} wynosi: {r2.pole}")
