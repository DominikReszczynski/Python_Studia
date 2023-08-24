"""1.Budka z lodami to szczególny rodzaj restauracji. Zdefiniuj klasę o nazwie
IceCreamStand dziedziczącą po klasie Restaurant. Dodaj atrybut o nazwie flavors,
przechowującą listę różnych smaków lodów. Zdefiniuj met odę wyświetlającą
dostępnesmaki lodów. Zaproponuj inne metody. Dodaj klasę o nazwie CoffeeShop
dziedzicząca po klasie Restaurant. Dodaj atrybut o nazwie coffee, przechowujący
listę różnych kaw np. americano, latte. Zdefiniuj metodę wyświetlającą dostępne
kawy. Zaproponuj metody. Zaproponuj utworzenie obiektów. Czy to zadanie wpisuje
się w zagadnienie abstrakcji,dziedziczenia, enkapsulacji oraz polimorfizmu?"""
class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        print(f"\nNazwa: {self.name}")
        print(f"typ: {self.type}\n")
    def open(self):
        print("Restauracja otwarta!")
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type) #super() służy do odwoływania się do klasy nadrzędnej (dziedziczenie)
        self.flavor = []
    def addFlavor(self,flavor):
        self.flavor.append(flavor)
    def displayFlavor(self):
        print("Dostępne smaki: ")
        for flavor in self.flavor:
            print(flavor)
class CoffeShop(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.coffe = []
    def addCoffe(self,coffe):
        self.coffe.append(coffe)
    def displayCoffe(self):
        print("Dostępne kawy: ")
        for coffe in self.coffe:
            print(coffe)

iceCreamStand=IceCreamStand("Lodziarnia Dżesika", "budka")
iceCreamStand.describe_restaurant()
iceCreamStand.displayFlavor()
iceCreamStand.addFlavor("czekolada")
iceCreamStand.addFlavor("truskawka")
iceCreamStand.addFlavor("vanilia")
iceCreamStand.displayFlavor()
DisplayCoffe=CoffeShop("Kawiarnia Cukrzyk","Stacjonarna")
DisplayCoffe.describe_restaurant()
DisplayCoffe.addCoffe("cappucino")
DisplayCoffe.addCoffe("czarna")
DisplayCoffe.addCoffe("biała")
DisplayCoffe.displayCoffe()
print("\nTak:\n"
      "Abstrakcja: klasy restauracja icecreamstand oraz coffeshop reprezentują abstrakcyjne pojęcie restauracji\n"
      "Dziedziczenie: klasa icecreamstand oraz coffeshop dziedziczą po klasie restaurant\n"
      "Enkapsulacja: atrybuty name oraz type ukrywane są w klasie restaurant ale sądostępne do odczytu i zmiany \n"
      "Polimorfizm: możemy traktować różne obiekty jako obiekty klasy bazowej \n")