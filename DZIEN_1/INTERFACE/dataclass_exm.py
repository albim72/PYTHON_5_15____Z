from dataclasses import dataclass,astuple,asdict,field

@dataclass(order=True)
class Person:
    firstname:str = "Jan"
    lastname:str = "Kot"
    age:int = 33
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    sort_index:int = field(init=False,repr=False)

    def __repr__(self):
        return f"Pracownik: {self.firstname} {self.lastname}, stanowisko: {self.job}"

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.sort_index = self.age



janek = Person()
print(janek)
print(janek.full_name)

benek = Person('Benedykt','Kowal',50,'CEO')
print(benek)
print(benek.full_name)

benedykt = Person('Benedykt','Kowal',55,'CEO')
print(benedykt)
print(benedykt.full_name)

print(benedykt>benek)

