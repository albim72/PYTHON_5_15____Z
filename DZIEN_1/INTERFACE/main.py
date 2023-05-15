from pojazd import Pojazd

p1 = Pojazd()
odl = 458
lt = 41
cena_l = 6.23

print(f'spalanie [l/100km]: {p1.spalanie100(odl,lt):.2f}')
print(f'koszt przejazdu na trasie {odl} km wynosi: {p1.kosztprzejazdu(odl,lt,cena_l):.2f} zł')
