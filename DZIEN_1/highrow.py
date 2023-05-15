#funkcje wyższego rządu -> to taka funkcja która posiada w atrybutach minimum jeden atrybut, który
#reprezentuje inną funkcję

liczby = [78,899,0,-456,111,99,8,-33,-80,56,789,0,111,-111,87,155,322,455,-222]

#stwórz nową listę parzyste i przkaż do niej te wartości z listy liczby, które są wartościami parzystmi

parzyste = list(filter(lambda x:x%2==0,liczby))
print(parzyste)

def nieparz(x):
    return x%2!=0

nparz = list(filter(nieparz,liczby))
print(nparz)

cube = list(map(lambda x:x**3,liczby))
print(cube)

#własna funkcja wyższego rzędu...

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik konkursu {imie}, liczba punktów: {punkty}"

def kierowca(imie,predkosc,pkarne):
    return f"kierowca {imie} jechał z prędkością {predkosc} km/h, i otrzymał punktów karnych {pkarne}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",66))
print(osoba(kierowca,"Piotr",145,12))
