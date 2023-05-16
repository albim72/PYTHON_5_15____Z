class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]

class RegularClass():
    pass

x = RegularClass()
y = RegularClass()
print(x,y)
print(x==y)

class SingletonClass(metaclass=Singleton):
    def __init__(self):
        self.opcja_k = 888

a = SingletonClass()
b = SingletonClass()
print(a,b)
print(a==b)

print(a.opcja_k)
print(b.opcja_k)

a.opcja_k = 222

print(a.opcja_k)
print(b.opcja_k)
