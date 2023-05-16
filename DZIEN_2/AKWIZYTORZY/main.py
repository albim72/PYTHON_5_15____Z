from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class Firma:
    def __repr__(self):
        return 'właściel formy otrzymuje wypłatę w formie dywidendy naliczanej raz w roku ' \
               '(na podstawie wyników finansowych)'

    def zarobek(self):
        return Decimal('7_500_000')


w = Firma()
a = Akwizytor('Adam','Kot','54353453453',Decimal('421_777'),Decimal('11.2'))
e = AkwizytorNaEtacie('Olga','Nowak','4354647878',Decimal('431_980'),Decimal('7.2'),Decimal('5500'))

prawcownicy = [a,e,w]
for prac in prawcownicy:
    print(prac)
    print(f'ZAROBEK: {prac.zarobek():.2f} zł')
