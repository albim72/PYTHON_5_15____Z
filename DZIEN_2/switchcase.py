class Switch(object):
    value = None
    def __new__(cls, value):
        cls.value = value
        return True

def case(*args):
    return any((arg==Switch.value for arg in args))

n = int(input("podaj cyfrę 1-10: "))

while Switch(n):
    if case(0):
        print("n jest równe 0")
        break
    if case(1,4,9):
        print("n jest kwadratem innej cyfry!")
        break
    if case(2):
        print("n jest liczbą parzystą...")
    if case(2,3,5,7):
        print("n jest liczbą pierwszą!")
        break
    if case(6,8):
        print("n jest krotnością liczby 2...")
        break
    print("pisz tylko cyfry!")
    break


