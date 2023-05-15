class ContextManager:
    def __init__(self):
        print("inicjacja metody init")

    def __enter__(self):
        print('inicjacja metody enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('inicjacja metody exit')

with ContextManager() as manager:
    print('blok wykonawczy instrukcji with')
