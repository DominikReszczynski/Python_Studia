"""Napisz klasę książka w której zdefiniujesz 5 obiektów dotyczących książek np. autor, tytuł Dodaj
5 metod, które będą wywoływane na obiektach z przekazywanymi parametrami np. czytaj();
Dodaj książki do list. Spróbuj utworzyć metody odpowiedzia
lne za sortowanie"""
title=[]
class book:
    species="książka"
    def __init__(self,autor,tytle,pages,binding):
        self.autor=autor
        self.tytle=tytle
        self.pages=pages
        self.binding=binding

    def read(self):
        return "czytasz książkę o tytule {}".format(self.tytle)
litlePrince= book("tomek","mały książę",159,"twarda")
oldMan= book("darek","stary człowiek i morze", 204,"miękka")
aldMan= book("darek","atary człowiek i morze", 204,"miękka")
title.append(litlePrince)
title.append(oldMan)
title.append(aldMan)
def sort (tab):
    operationTab=[]
    sizd=len(tab)

    for i in range(sizd):
        tytle = tab[i].tytle
        operationTab.append(tytle)
    operationTab.sort()
    return operationTab




print(litlePrince.read())
print(title)
print(oldMan.tytle)
print("sortowanie po tytułach", sort(title))