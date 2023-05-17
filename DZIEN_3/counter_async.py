import asyncio
import time

async def count():
    print("jeden")
    await asyncio.sleep(1)
    print("drugi")

async def main():
    await asyncio.gather(count(),count(),count())

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} wykonany w czasie {elapsed:.2f} s")
