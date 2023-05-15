from oldresistor import OldResistor

print("Różne konstrukcje klas i ich metod....")
r0 = OldResistor(10.2E2)
print(f"_____________ {r0.__class__.__name__} ____________")
print(r0)
r0.set_ohms(5.1E3)
print(f"noa wartość oporu: {r0.get_ohms()} omów")
