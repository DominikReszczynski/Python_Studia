"""Napisz klasę Pojazd, która będzie klasą bazową oraz dwie
podklasy : samochód oraz motocykl. Utwórz prosty konstruktor oraz destruktor.
Podklasy będą dziedziczyły puste pole : nr_tablica odpowiadający za
przypisanie tablicy rejestracyjnej. Destruktor będzie odpowiadał za usunięcie
obiektów z pamięci procesora po wykonaniu programu.
Dodaj metody, które według Ciebie pozwolą w pełni pokazać dziedziczenie."""
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

class car(Vehicle):
    def __int__(self,speed):
        super().__init__(speed)
    def highway(self):
        speede= self.speed+190
        print("Jestem zmodowany, dzięki temu mogę jechać w tym momencie", speede,"km/h")
    def __del__(self):
        print("Tu",self.brand,"chciałem nauczyć się latać i wylądowałem na drzewie")
class motor(Vehicle):
    def __int__(self,speed):
        super().__init__(speed)
    def speedTest(self):
        print("Speed test wykazał:", self.speed,"km/h")
    def __del__(self):
        print("Speed test wykazał:", self.speed + 1,"km/h, motor", self.brand,"nie przetrwał takiej szybkości!")
motor=motor("honda",190) #konstruktor klasy
motor.speedTest()

mercedes=car("mercedes",210) #konstruktor klasy
mercedes.highway()
del mercedes #destruktor klasy
del motor #destruktor klasy

"""class bird:
    def __init__ (self, gatunek, szybkość):
        self.gatunek = gatunek
        self.szybkość = szybkość
    def fly(self):
        print ("Tu", self.gatunek, ".Lecimy i osiągniemy prędkość", self.szybkość)
class eagle (bird):
    def __init__ (self, szybkość):
        super().__init__("orzeł", szybkość)
    def attack(self):
        print ("Tu", self.gatunek, ". Do atakuuuuu!")
class penguin (bird):
    def __init__ (self, szybkość):
        super().__init__("pingwin", szybkość)
    def slide(self):
        print ("Tu", self.gatunek, ". Bziuuuuum")
    def fly(self):
        print ("Tu", self.gatunek, ".Nie potrafię latać :((")
orzel = eagle(90)
orzel.fly()
orzel.attack()
pingwin = penguin(50)
pingwin.slide()
pingwin.fly()"""