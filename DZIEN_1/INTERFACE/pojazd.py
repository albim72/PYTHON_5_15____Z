from ipojazd import IPojazd

class Pojazd(IPojazd):
    def spalanie100(self, odl, litry):
        return litry*100/odl

    def kosztprzejazdu(self, odl, litry, cena_l):
        return self.spalanie100(odl,litry)*(odl/100)*cena_l
