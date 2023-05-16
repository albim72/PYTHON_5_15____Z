from dataclasses import dataclass

@dataclass
class Article:
    title:str
    author:str
    content:str
    press:str

    def __repr__(self):
        return f'{self.title} {self.author} {self.content}'

@dataclass(init=False)
class PythonArticle(Article):
    # language:str
    # author:str
    # price:int=30

    def __repr__(self):
        return f"{self.language} {self.author} {self.price} zł"

    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "Opis wybranych aspektów użycia języka Python"

    def infoarticle(self):
        return f'Publikacja {self.title}, autor: {self.author}, rabat 10%: {0.1*self.price:.2f},' \
               f'do zapłaty: {0.9*self.price:.2f} zł'

    # def wydawnictwo(self):
    #     return f"wydawnictwo: {self.press}"
    #
    # def setpress(self,wyd):
    #     self.press = wyd
    @property
    def wydawnictwo(self):
        return self.press

    @wydawnictwo.setter
    def wydawnictwo(self,nazwa):
        self.press = nazwa

art = Article("Typowanie w Pythonie","Marcin Albiniak","kilka słów o typowaniu...","ABC")
print(art)

pyart = PythonArticle("Algorytmy AI w Pythonie",68)
pyart.wydawnictwo = "XYZ"
print(pyart)
print(pyart.infoarticle())
print(pyart.wydawnictwo)
