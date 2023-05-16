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
        
    @property
    def sprzedaz(self):
        return self._sprzedaz
    
    
    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota < Decimal('0.00'):
            raise ValueError('Wartość sprzedaży nie może być ujemna!')
        self._sprzedaz = kwota
        
    @property
    def prowizja(self):
        return self._prowizja
    
    @prowizja.setter
    def prowizja(self,procent):
        if not (Decimal('0.0')<=procent<=Decimal('25.0')):
            raise ValueError('prowizja nie może być mniejsza bądź równa 0 i nie może przekraczać wartości 25%')
        self._prowizja = procent
        
    def zarobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.0'))
    
    def __repr__(self):
        return ('Akwizytor: ' +
                f'{self.imie} {self.nazwisko}\n'
                f'numer ubezpieczenia: {self.nr_ubezpieczenia}\n'
                f'sprzedaż: {self.sprzedaz:.2f} zł\n'
                f'prowizja: {self.prowizja:.2f} %')






