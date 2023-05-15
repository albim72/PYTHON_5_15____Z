from datetime import date

class Osoba:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    @classmethod
    def ile_lat(cls,imie,rok):
        return cls(imie,date.today().year - rok)

    @staticmethod
    def czydorosly(wiek):
        return wiek>=18

pr1 = Osoba('Roman',67)
pr2 = Osoba.ile_lat('Anna',1979)

print(pr1.wiek)
print(pr2.wiek)

print(type(pr1))
print(type(pr2))

print(Osoba.czydorosly(23))
print(pr1.czydorosly(pr1.wiek))
print(pr2.czydorosly(pr2.wiek))
