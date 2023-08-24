"""2.Napisz program reprezentujący obiektowo system oceniający
produkty pochodzące z klasy Beer. Zaproponuj poszczególne pola np. kategorie,
stężenie procentowe, cenę, miejsce na opinię. Zaproponuj możliwość sortowania
według ocen oraz nazw.Zaproponuj klasę Sklep. Jakie metody i pola zaproponujesz
by klasa Beer mogłaby wykorzystywać klasę Sklep?"""


class Beer:
    def __init__(self, name, strength, price, star):
        self.name = name
        self.strength = strength
        self.price = price
        self.star = star

    def getName(self):
        return self.name

    def getStar(self):
        return self.star

    def info(self):
        print(f"Nazwa: {self.name} \nMoc: {self.strength} \nCena: {self.price} \nGwiazdki: {self.star}\n")

    def __str__(self):
        return f"Nazwa: {self.name}, Ocena: {self.star}"


class Shop:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def addBeer(self, beer):
        self.inventory.append(beer)

    def removeBeer(self, beer):
        self.inventory.remove(beer)

    def findBeerByName(self, name):
        for beer in self.inventory:
            if beer.getName() == name:
                return beer
        return None


class beerRating:
    def __init__(self):
        self.beer = []

    def addBeer(self, beer):
        self.beer.append(beer)

    def sortByRating(self):
        sortedBeers = sorted(self.beer, key=lambda x: x.getStar(), reverse=True)
        print("Wyświetlę teraz piwa posortowane według oceny użytkowników:\n")
        for beer in sortedBeers:
            beer.info()
        print("------------------------------------------------")

    def sortByName(self):
        sortedBeers = sorted(self.beer, key=lambda x: x.getName())
        print("Wyświetlę teraz piwa posortowane według nazwy:\n")
        for beer in sortedBeers:
            beer.info()
        print("------------------------------------------------")


beer1 = Beer("Heineken", 5.0, 2.5, 4.5)
beer2 = Beer("tyskie", 4.2, 3.0, 4.8)
beer3 = Beer("zubr", 6.2, 4.5, 4.2)

rating = beerRating()
rating.addBeer(beer1)
rating.addBeer(beer2)
rating.addBeer(beer3)

sklep = Shop("Sklep u Mariana")
sklep.addBeer(beer1)
sklep.addBeer(beer2)
sklep.addBeer(beer3)

searchedBeer = sklep.findBeerByName("tyskie")
if searchedBeer is not None:
    print("Znalezione piwo:")
    searchedBeer.info()
else:
    print("Nie znaleziono piwa o podanej nazwie.")

rating.sortByRating()
rating.sortByName()
