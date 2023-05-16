import json

prac =  """{
            "imie": "Benedykt",
            "nazwisko": "Knot",
            "stanowisko": "elektryk",
            "lata_pracy": 12,
            "email": "knotek@firma.pl"
        }"""

print(prac)
print(type(prac))

pracdict = json.loads(prac)
print(pracdict)
print(type(pracdict))
print(pracdict['stanowisko'])
pracdict['stanowisko'] = "starszy elektryk"

json_prc = json.dumps(pracdict,indent=4)
print(json_prc)

