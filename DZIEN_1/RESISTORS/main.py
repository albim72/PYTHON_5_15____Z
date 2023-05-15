from oldresistor import OldResistor
from resistor import Resistor
from votage import VoltageResistance
from bounded import BoundedResistance

print("Różne konstrukcje klas i ich metod....")
r0 = OldResistor(10.2E2)
print(f"_____________ {r0.__class__.__name__} ____________")
print(r0)
r0.set_ohms(5.1E3)
print(f"noa wartość oporu: {r0.get_ohms()} omów")

r1 = Resistor(50E3)
print(f"_____________ {r1.__class__.__name__} ____________")
r1.ohms = 7.7E2
print(r1.ohms)

print(f"układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V\n"
      f"natężenie prądu: {r1.current} A")

r2 = VoltageResistance(1E3)
print(f"_____________ {r2.__class__.__name__} ____________")
print(f"natężenie początkowe prądu: {r2.current} A")
r2.voltage = 48
print(f"natężenie prądu: {r2.current} A")
print(f"napięcie prądu: {r2.voltage} V")

r3 = BoundedResistance(1E2)
print(f"_____________ {r3.__class__.__name__} ____________")
try:
      r3.ohms = -10
      print(f'oporność: {r3.ohms}om')
except ValueError as ve:
      print(ve)
except Exception as exc:
      print(exc)

print("ciąg dalszy programu....")
