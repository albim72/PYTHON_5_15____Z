import time
import concurrent.futures
from suma_liczb_p import znajdz_sume_liczb_pierwszych

numbers = [(1,10_000),(3,50_000),(5_000,100_000),(4,900),(800,15_000),(95_000,167_900)]

def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)

def synchroniczna():
    starttime=time.time()
    for pair in numbers:
        prime_suma = znajdz_sume_liczb_pierwszych(*pair)
        print(prime_suma)
    endtime = time.time()
    print(f"całkowity czas wykoania obliczenia w procesie synchronicznym wynosi: {endtime-starttime:.2f} s")

def asynchroniczna_proc():
    starttime = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    print(list(wynik))
    endtime = time.time()
    print(f"całkowity czas wykoania obliczenia w procesie asynchronicznym wynosi: {endtime - starttime:.2f} s")

def asynchroniczna_thread():
    starttime = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    print(list(wynik))
    endtime = time.time()
    print(f"całkowity czas wykoania obliczenia w procesie asynchronicznym wynosi: {endtime - starttime:.2f} s")


def main():
    synchroniczna()
    asynchroniczna_proc()
    asynchroniczna_thread()

if __name__ == '__main__':
    main()
