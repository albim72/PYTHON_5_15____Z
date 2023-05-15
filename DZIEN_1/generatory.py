#przykład 1
def liczby():
    for i in range(17):
        yield i*2

for p in liczby():
    print(p)

#przykład 2
def wznowienie(n,k):
    print("wstrzymanie działania...")
    yield 1002
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n+k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n*k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield 3*n/(k-1)
    print("wznowienie działania...")

for i in wznowienie(4,8):
    if i==1002:
        continue
    print(f"zwrócono wartość: {i}")
