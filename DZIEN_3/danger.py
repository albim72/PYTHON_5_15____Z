import os

fragmentkodu = """
a=5
b=15
print(f'a x b = {a*b}')
"""

exec(fragmentkodu)

code = input("co chcesz dzisiaj napisać?")
exec(code)

def policzPole(l):
    return l**2

def policzObwod(l):
    return 4*l

expr = input("podaj funkcję: ")
for l in range(1,5):
    if(expr=='policzPole(l)'):
        print(f"jeśli długość boku to {l} m pole działki wynosi: {eval(expr)}")
    elif (expr=='policzObwod(l)'):
        print(f"jeśli długość boku to {l} m obwód działki wynosi: {eval(expr)}")
    else:
        print("Zła funkcja")
        break
        
