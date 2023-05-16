class MojaMeta(type):
    def __new__(cls, clsname,bases,attrib):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy:{bases}")
        print(f"zbiór atrybutów: {attrib}")
        return type.__new__(cls, clsname,bases,attrib)
    def info(cls):
        return "metaklasa działa..."

class Zwykla:
    def oblicz(self,x,y):
        return x+y


class Pierwsza(Zwykla,metaclass=MojaMeta):
    def oblicz(self, x, y):
        return super().oblicz(x, y) - 2

class Druga(Pierwsza):
    pass

class Dodatkowa:
    pass

class Trzecia(Dodatkowa,Druga):
    pass
