from decimal import Decimal

class Akwizytor:
    """
    pracownik którego wynagrodzenie jest wyłącznie prowiją od sprzedaży
    """
    def __init__(self,imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja
        
    @property
    def imie(self):
        return self._imie
    
    @imie.setter
    def imie(self,nimie):
        self._imie = nimie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nnaz):
        self._nazwisko = nnaz

    @property
    def nr_ubezpieczenia(self):
        return self._nr_ubezpieczenia

    @nr_ubezpieczenia.setter
    def nr_ubezpieczenia(self, nr):
        self._nr_ubezpieczenia = nr
    
    
        
        
        
        
        
