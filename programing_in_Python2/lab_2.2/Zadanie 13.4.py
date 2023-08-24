"""Napisz program, w którym spróbujesz zamodelować otaczającą Cię rzeczywistość.
Napisz klasę student, w której zdefiniujesz obiekty dotyczące studenta. Jakie to będą obiekty? Dodaj
metody,które będą wywoływane na obiektach z przekazywanymi parametrami. Jakimi
parametrami?"""
class student:
    def __init__(self,name,secondName,age,field):
        self.fullName=name+" "+secondName
        self.age=age
        self.field=field
    def studie(self, what):
        return "student {} uczy się {} na studia {}".format(self.fullName, what, self.field)
    def howMuchToEnd(self,semestrs):
        howManySemestrs=7-semestrs
        return "Do końca studiów uczniowi {} zostało {} semestrów".format(self.fullName,howManySemestrs)
Dominik=student("Dominik","Reszczyński",21,"informatyka")
print(Dominik.studie("programować"))
print(Dominik.howMuchToEnd(2))