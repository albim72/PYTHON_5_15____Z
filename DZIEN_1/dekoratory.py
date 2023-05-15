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

def pomiarczasu(funkcja):
    def wrapper():
        start = time.perf_counter()
        funkcja()
        end = time.perf_counter()
        print(f"czas wykonania funkcji {end-start} s")
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja: {funkcja.__name__}')
        print(funkcja(*args))
    return wrapper

@sleep
@pomiarczasu
# @debug
def big_lista():
    sum([i**2 for i in range(1_000_000)])

big_lista()


@debug
def info(msg):
    return f"nowa wiadomość: {msg}"

info('masz paczkę!')
