liczby = [56,9009,-1003,0,53,-3,23,456,123,-452,99,101,34,6,-1,34,654,333]

def moje_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum-minimum
    suma = sum(lista)
    lelem = len(lista)
    sr_artm = suma/lelem
    return minimum,maksimum,rozstep,suma,lelem,sr_artm

wynik = moje_statystyki(liczby)
print(wynik)
print(type(wynik))

mini, maxi, roz, sm, el, sa = moje_statystyki(liczby)
print(f"wartość maksymalna: {maxi}, wartość minimalna: {mini}, rozstęp: {roz}, "
      f"suma wartości elementów: {sm}, liczba elementów: {el}, średnia arytmetyczna: {sa}")
