class MonoBase(type):
    def __new__(cls, clsname, bases, attrs):
        if len(bases)>1:
            raise TypeError("Możliwe jest tylko jednodziedziczenie!!!")
        return super().__new__(cls, clsname, bases, attrs)


class Base(metaclass=MonoBase):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(B):
    pass

class Moja:
    pass

class MMM(Moja,C):
    pass
