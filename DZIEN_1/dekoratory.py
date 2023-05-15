import time
import math

#przykład prostego dekoratora
def startstop(funkcja):
    def wrapper(*args):
        print("start procesu...")
        funkcja(*args)
        print("koniec procesu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w seberka...")

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} w urodziny...")


dmuchanie("świeczek")

#dekorator opisujący pomiar czasu

def pomiarczasu(funckja):
    def wrapper():
        start = time.perf_counter()
        funckja()
        end = time.perf_counter()
        print(f"czas wykonania funkcji {end-start} s")
    return wrapper
