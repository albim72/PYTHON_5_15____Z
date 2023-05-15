from dataclasses import dataclass, Field
from datetime import datetime

#opis klasy Field ->  'default','default factory','init','repr','hash','compare','metadata','kw_only' - od wersji 10

params = {
    'name':Field(None,None,True,True,True,True,None),
    'surname':Field(None,None,True,True,True,True,None),
    'year_of_birth':Field(None,None,True,True,True,True,None),
}

def age(self):
    return datetime.now().year - self.year_of_birth

#dataclass(type(nazwa_klasy,dziedziczone klasy, atrybutyklasy /metody, właściwości, konstruktor.../)
Person = dataclass(type('Person',(),{'__annotations__':params, 'age':property(age)}))

p = Person('Romualda','Tracz',1956)
print(p)
print(p.age)
