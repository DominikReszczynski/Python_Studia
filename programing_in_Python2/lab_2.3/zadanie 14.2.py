"""Napisz program, w którym utworzysz klasę podstawową : Zwierzę
oraz klasy potomne:kot, pies, ptak, ryba.
Zaproponuj odpowiednie metody, pola i dziedziczenie"""
class Animal:
    def __init__ (self, species, name, age):
        self.species = species
        self.name = name
        self.age= age
class dog (Animal):
    def __init__ (self, name,age):
        super().__init__("pies", name,age)
        print("jestem:", self.species, "\nna imię mam:", self.name, "\nmam lat:", self.age,"\n")
    def canI(self):
        print("czy", self.species,"może na dwór?\nJASNE ŻE MOGĘ!!!")
    def __del__(self):
        print("\nNiestety, dożyłem swego wieku drogi użytkowniku.\nW dlaszą wędrówkę musisz iść sam:(\n",self.name)
class cat (Animal):
    def __init__ (self, name,age):
        super().__init__("kot", name,age)
        print("jestem:", self.species, "\nna imię mam:", self.name, "\nmam lat:", self.age,"\n")
    def canI(self):
        print("czy", self.species,"może na dwór?\nJASNE ŻE MOGĘ!!!")
    def __del__(self):
        print("\nNiestety, dożyłem swego wieku drogi użytkowniku.\nW dlaszą wędrówkę musisz iść sam:(\n",self.name)
class fish (Animal):
    def __init__ (self, name, age):
        super().__init__("ryba", name,age)
        print("jestem:",self.species,"\nna imię mam:", self.name,"\nmam lat:", self.age,"\n")
    def canI(self):
        print("czy", self.species,"może na dwór?\nNIESTETY NIEMOGĘ")
    def __del__(self):
        print("\nNiestety, dożyłem swego wieku drogi użytkowniku.\nW dlaszą wędrówkę musisz iść sam:(\n",self.name)
fishie=fish("Ara",14)
fishie.canI()
del fishie
dogie=dog("Rufus",2.5)
dogie.canI()
del dogie
catie=cat("Miki",6)
catie.canI()
del catie





